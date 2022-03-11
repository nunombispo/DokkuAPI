import os
import signal
import subprocess
from socket import socket


def run_command(command, timeout=60):
    daemon_socket = '/tmp/socket_test.s'
    if not os.path.exists(daemon_socket):
        return False, 'Dokku daemon is not running'
    x = command
    client = socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect("/tmp/socket_test.s")
    print("SEND:", x)
    client.send(x.encode('utf-8'))
    result = client.recv(1024)

    return True, result.decode('utf-8')
