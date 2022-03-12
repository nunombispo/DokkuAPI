import os
import socket
from paramiko.client import SSHClient, AutoAddPolicy
from config import settings


ssh_hostname = settings.SSH_HOSTNAME
ssh_port = settings.SSH_PORT
ssh_key_path = settings.SSH_KEY_PATH
ssh_key_passphrase = settings.SSH_KEY_PASSPHRASE


def __execute_command(command, username):
    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(ssh_hostname, ssh_port, username=username,
                       key_filename=ssh_key_path, passphrase=ssh_key_passphrase)
        if username == 'root':
            command = 'dokku ' + command
        stdin, stdout, stderr = client.exec_command(command, timeout=60)
        output = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()
        if output:
            return True, output
        else:
            return False, error
        client.close()
    except Exception as e:
        return False, str(e)


def run_command(command):
    success, message = __execute_command(command, 'dokku')
    return success, message


def run_root_command(command):
    success, message = __execute_command(command, 'root')
    return success, message



