from sys import stdout
from daemon.daemon import run_command
import json


def __execute_command(command):
    stdout.write(f'\nExecuting command: {command}\n')
    success, message = run_command(command)
    stdout.write(f'Execution result: {success}\n')
    stdout.write(f'Output: {message}\n')
    if success:
        if message is not None:
            json_output = json.loads(message)
            stdout.write(f'JSON: {json_output}\n')
            success = True if json_output['ok'] == 'True' else False
            message = json_output['output']
    return success, message


# Creates an application
def create_app(app_name):
    command = f'apps:create {app_name}'
    success, message = __execute_command(command)
    return success, message
