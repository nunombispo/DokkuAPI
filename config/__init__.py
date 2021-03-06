# Import BaseSettings from pydantic
from decouple import config
from pydantic import BaseSettings


# Define the CommonSettings class (inherits from BaseSettings)
class CommonSettings(BaseSettings):
    API_NAME: str = config('API_NAME')
    API_VERSION_NUMBER: str = config('API_VERSION_NUMBER')


# Define the ServerSettings class (inherits from BaseSettings)
class ServerSettings(BaseSettings):
    SSH_HOSTNAME: str = config('SSH_HOSTNAME')
    SSH_PORT: int = config('SSH_PORT', cast=int)
    SSH_KEY_PATH: str = config('SSH_KEY_PATH')
    SSH_KEY_PASSPHRASE: str = config('SSH_KEY_PASSPHRASE')


# Define the DatabaseSettings class (inherits from BaseSettings)
class DatabaseSettings(BaseSettings):
    pass


# Main Settings class that includes all the settings classes
class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    API_KEY: str = config('API_KEY')


# We create a settings variable that will be used in the other files
settings = Settings()
