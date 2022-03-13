from sys import stdout
from commands.ssh import run_command, run_root_command


def __execute_command(command):
    stdout.write(f'\nExecuting command: {command}\n')
    success, message = run_command(command)
    stdout.write(f'Result: {success}\n')
    stdout.write(f'Output: {message}\n')
    return success, message


def __execute_root_command(command):
    stdout.write(f'\nExecuting root command: {command}\n')
    success, message = run_root_command(command)
    stdout.write(f'Result: {success}\n')
    stdout.write(f'Output: {message}\n')
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


# List plugins
def list_plugins():
    command = 'plugin:list'
    success, message = __execute_command(command)
    return success, message


# Check if a plugin is installed
def is_plugin_installed(plugin_name):
    success, message = list_plugins()
    if success:
        for plugin in message.split('\n'):
            if plugin_name in plugin:
                return True, 'Plugin is installed'
        return False, 'Plugin is not installed'
    return False, message


# Install a plugin
def install_plugin(plugin_name):
    if plugin_name == 'postgres':
        command = 'plugin:install https://github.com/dokku/dokku-postgres.git'
    elif plugin_name == 'mysql':
        command = 'plugin:install https://github.com/dokku/dokku-mysql.git mysql'
    else:
        return False, 'Plugin not found'
    success, message = __execute_root_command(command)
    return success, message


# Uninstall a plugin
def uninstall_plugin(plugin_name):
    command = f'plugin:uninstall {plugin_name}'
    success, message = __execute_root_command(command)
    return success, message


# Create a database
def create_database(plugin_name, database_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'{plugin_name}:create {database_name}'
    success, message = __execute_command(command)
    return success, message


# List databases
def list_databases(plugin_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'{plugin_name}:list'
    success, message = __execute_command(command)
    return success, message


# Check if a database exists
def database_exists(plugin_name, database_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    success, message = list_databases(plugin_name)
    if success:
        for database in message.split('\n'):
            if database_name in database:
                return True, 'Database exists'
        return False, 'Database does not exist'
    return False, message


# Delete a database
def delete_database(plugin_name, database_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'--force {plugin_name}:destroy {database_name}'
    success, message = __execute_command(command)
    return success, message


# List linked apps
def database_linked_apps(plugin_name, database_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'{plugin_name}:links {database_name}'
    success, message = __execute_command(command)
    return success, message


# Link database to an app
def link_database(plugin_name, database_name, app_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'{plugin_name}:link {database_name} {app_name}'
    success, message = __execute_command(command)
    return success, message


# Unlink database from an app
def unlink_database(plugin_name, database_name, app_name):
    if plugin_name != 'postgres' and plugin_name != 'mysql':
        return False, 'Plugin not found'
    command = f'{plugin_name}:unlink {database_name} {app_name}'
    success, message = __execute_command(command)
    return success, message


