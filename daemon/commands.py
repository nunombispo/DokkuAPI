from sys import stdout
from daemon.daemon import run_command


def __execute_command(command):
    stdout.write(f'\nExecuting command: {command}\n')
    success, message = run_command(command)
    stdout.write(f'Result: {success}\n')
    stdout.write(f'Output: {message}')
    return success, message


# Creates an application
def create_app(app_name):
    command = f'apps:create,{app_name}'
    success, message = __execute_command(command)
    return success, message


# Deletes an application
def delete_app(app_name):
    command = f'--force,apps:destroy,{app_name}'
    success, message = __execute_command(command)
    return success, message


# Lists all applications
def list_apps():
    command = 'apps:list'
    success, message = __execute_command(command)
    return success, message

