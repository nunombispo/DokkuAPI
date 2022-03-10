from sys import stdout
from daemon.daemon import run_command
import json


def __execute_command(command):
    stdout.write(f'Executing command: {command}')
    success, message = run_command(command)
    stdout.write(f'Success: {success}')
    stdout.write(f'Message: {message}')
    if success:
        json_output = json.loads(message)
        stdout.write(f'JSON: {json_output}')
        success = True if json_output['ok'] == 'true' else False
        message = json_output['output']
    return success, message


# Creates an application
def create_app(app_name):
    command = f'apps:create {app_name}'
    success, message = __execute_command(command)
    return success, message
