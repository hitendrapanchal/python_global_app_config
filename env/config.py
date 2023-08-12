from typing import get_type_hints, Union
import env.loadconfig as loadconfig

#IMPORTANT: Ensure APP_ENV is passed into operating system environment variable

class ApplicationConfiguration:

    # Environment Merge Rule : .env  +   .env.{APP_ENV} + os.environ
    # Example : .env + .env.prod + os.environ
    
    """
    Environment mapping to variables to class fields will follow below rules:
      - CAPs field will be only considered else skipped 
      - Class field and environment variable name are the same
      - Field won't be parsed unless it has a type annotation
    """

    #********************************
    # Dict which contains all keys and value 
    #********************************
    appConfigs: {}

    #********************************
    # Common Keys which are not environment specific 
    # and applicable to all envs
    #********************************
    APP_ENV:str
    APP_DATE_FORMAT: str ='utc'

    #********************************
    # Database configuration
    #********************************
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_DATABASE_PEM: str 

    #********************************
    # APIs
    #********************************
    MODEL_API_KEY:str
    MODEL_API_URL:str
    API_URL:str

    def __init__(self, env):
        print("Populating configuration in Config")
        for field in self.__annotations__:
            if not field.isupper():
                continue

            # Raise AppConfigError if required field not supplied
            default_value = getattr(self, field, None)
            if default_value is None and env.get(field) is None:
                raise ApplicationConfigurationError('The {} field is required'.format(field))

            # Cast env var value to expected type and raise AppConfigError on failure
            try:
                var_type = get_type_hints(ApplicationConfiguration)[field]
                if var_type == bool:
                    value = _parse_bool(env.get(field, default_value))
                else:
                    value = var_type(env.get(field, default_value))

                self.__setattr__(field, value)
            except ValueError:
                raise ApplicationConfigurationError('Unable to cast value of "{}" to type "{}" for "{}" field'.format(
                    env[field],
                    var_type,
                    field
                )
            )
            self.appConfigs=env

    def __repr__(self):
        return str(self.__dict__)

class ApplicationConfigurationError(Exception):
    pass

def _parse_bool(val: Union[str, bool]) -> bool:  # pylint: disable=E1136 
    return val if type(val) == bool else val.lower() in ['true', 'yes', '1']

app_env_configs=loadconfig.loadConfiguration()
Config = ApplicationConfiguration(app_env_configs)












