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
    elif plugin_name == 'letsencrypt':
        command = 'plugin:install https://github.com/dokku/dokku-letsencrypt.git'
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


# Set domain for an app
def set_domain(app_name, domain):
    command = f'domains:set {app_name} {domain}'
    success, message = __execute_command(command)
    return success, message


# Remove domain for an app
def remove_domain(app_name, domain):
    command = f'domains:remove {app_name} {domain}'
    success, message = __execute_command(command)
    return success, message


# Set LetsEncrypt mail
def set_letsencrypt_mail(email):
    command = f'config:set --global DOKKU_LETSENCRYPT_EMAIL={email}'
    success, message = __execute_command(command)
    return success, message


# Enable LetsEncrypt for an app
def enable_letsencrypt(app_name):
    command = f'letsencrypt:enable {app_name}'
    success, message = __execute_command(command)
    if 'retrieval failed' in message:
        return False, message
    return success,


# Enable LetsEncrypt auto renewal
def enable_letsencrypt_auto_renewal():
    command = f'letsencrypt:cron-job --add'
    success, message = __execute_command(command)
    return success, message


# List application configurations
def config_show(app_name):
    command = f'config:show {app_name}'
    success, message = __execute_command(command)
    return success, message


# Set application configuration key
def config_set(app_name, key, value):
    command = f'config:set --no-restart {app_name} {key}={value}'
    success, message = __execute_command(command)
    return success, message


# Set application configuration from file
def config_file(app_name, contents):
    keys = ''
    cleaned_contents = contents.decode('utf-8').replace('\r', '')
    list_of_lines = cleaned_contents.split('\n')
    for line in list_of_lines:
        if line != '':
            if line.startswith('#'):
                continue
            keys = keys + line + ' '
    command = f'config:set --no-restart {app_name} {keys}'
    success, message = __execute_command(command)
    return success, message


# Apply application configuration
def config_apply(app_name):
    command = f'ps:rebuild {app_name}'
    success, message = __execute_command(command)
    return success, message

