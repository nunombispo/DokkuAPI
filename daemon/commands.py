from daemon.daemon import run_command
import json


def create_app(app_name):
    command = f'apps:create {app_name}'
    success, message = run_command(command)
    if success:
        json_output = json.loads(message)
        success = True if json_output['ok'] else False
        message = json_output['output']
    return success, message
