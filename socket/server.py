import socket
import os.path
import subprocess

daemon_socket = "/var/run/dokku-api/daemon.sock"


def setup_server():
    if os.path.exists(daemon_socket):
        os.remove(daemon_socket)
    else:
        os.makedirs(os.path.dirname(daemon_socket), exist_ok=True)
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(daemon_socket)
    return server


def validate_data(data):
    if data == "":
        return False, "No data received".encode('utf-8')
    if 'destroy' in data and '--force' not in data:
        return False, "Command `destroy` requires --force".encode('utf-8')
    return True, "Data is valid".encode('utf-8')


def process_command(command):
    command_list = command.split(',')
    command_list.insert(0, 'dokku')
    ps = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = ps.communicate(timeout=60)
    if ps.returncode == 0:
        return True, out
    else:
        return False, err


def main():
    server = setup_server()
    while True:
        try:
            server.listen(1)
            connection, address = server.accept()
            data = connection.recv(4096)
            if data:
                data = data.decode('utf-8')
                valid, message = validate_data(data)
                if valid:
                    success, output = process_command(data)
                    if success:
                        result = {'status': True, 'output': output}
                    else:
                        result = {'status': False, 'output': output}
                else:
                    result = {'status': False, 'output': message}
                encoded_result = str(result).encode('utf-8')
                connection.send(encoded_result)
            connection.close()
        except KeyboardInterrupt:
            connection.close()
            break
        except Exception as e:
            connection.send(str(e).encode('utf-8'))
            connection.close()
    server.close()


if __name__ == '__main__':
    main()

