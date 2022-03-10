from sys import stdout
from daemon.daemon import run_command
import json


def __execute_command(command):
    stdout.write(f'\nExecuting command: {command}\n')
    success, message = run_command(command)
    stdout.write(f'Result: {success}\n')
    stdout.write(f'Output: {message}')
    if success:
        if message is not None and message != '':
            json_output = json.loads(message)
            stdout.write(f'JSON: {json_output}\n\n')
            success = json_output['ok']
            message = json_output['output']
    return success, message


# Creates an application
def create_app(app_name):
    command = f'apps:create {app_name}'
    success, message = __execute_command(command)
    return success, message


# Deletes an application
def delete_app(app_name):
    command = f'--force apps:destroy {app_name}'
    success, message = __execute_command(command)
    return success, message


# Lists all applications
def list_apps():
    command = 'apps:list'
    success, message = __execute_command(command)
    return success, message

