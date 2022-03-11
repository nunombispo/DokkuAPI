
import socket
import os, os.path
import subprocess

if os.path.exists("/tmp/socket_test.s"):
    os.remove("/tmp/socket_test.s")

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind("/tmp/socket_test.s")
while True:
    server.listen(1)
    conn, addr = server.accept()
    datagram = conn.recv(1024)
    if datagram:
        print(datagram)
        list = datagram.decode('utf-8').split(',')
        print(list)
        process = subprocess.Popen(list,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stdout)
        conn.send(stdout)
        conn.close()

