from daemon.daemon import run_command


def create_app(app_name):
    command = f'apps:create {app_name}'
    success, output = run_command(command)
    return success, output

