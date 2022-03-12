import os
import socket
from paramiko.client import SSHClient, AutoAddPolicy
from config import settings


ssh_hostname = settings.SSH_HOSTNAME
ssh_port = settings.SSH_PORT
ssh_key_path = settings.SSH_KEY_PATH
ssh_key_passphrase = settings.SSH_KEY_PASSPHRASE


def run_command(command):
    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(ssh_hostname, ssh_port, username='dokku',
                       key_filename=ssh_key_path, passphrase=ssh_key_passphrase)
        stdin, stdout, stderr = client.exec_command(command, timeout=60)
        output = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()
        if error:
            return False, error
        else:
            return True, output
        client.close()
    except Exception as e:
        return False, str(e)



