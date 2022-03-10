import os
import signal
import subprocess


def run_command(command, timeout=60):
    daemon_socket = '/var/run/dokku-daemon/dokku-daemon.sock'
    if not os.path.exists(daemon_socket) or not os.access(daemon_socket, os.W_OK):
        return False, 'Dokku daemon is not running'

    subprocess_command = [
        'nc',
        '-q', '1',            # time to wait after eof
        '-w', '60',            # timeout
        '-U', daemon_socket,  # socket to talk to
    ]

    ps = subprocess.Popen(['echo', command], stdout=subprocess.PIPE)

    with subprocess.Popen(
            subprocess_command,
            stdin=ps.stdout,
            stdout=subprocess.PIPE,
            preexec_fn=os.setsid) as process:
        try:
            output = process.communicate(timeout=timeout)[0]
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGINT)  # send signal to the process group
            output = process.communicate()[0]
    ps.wait(timeout)

    return ps.returncode == 0, output.decode('utf-8')

