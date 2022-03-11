import os
import socket
from config import settings


daemon_socket = settings.DAEMON_SOCKET_PATH


def run_command(command):
    if not os.path.exists(daemon_socket):
        return False, 'Dokku daemon is not running'

    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        client.connect(daemon_socket)
        client.send(command.encode('utf-8'))
        result = client.recv(4096)
    except Exception as e:
        return False, str(e)

    return True, result.decode('utf-8')

