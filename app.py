import os
os.environ["APP_ENV"] = "qa"
#Ensure environ["APP_ENV"] is set during deployment or before application start to load configuratio in Config object 

from env.config import Config
from test_app.test_config import ShowAPIkeys_test



def showconfiguration_test():
    
    print('Config.API_URL:         {}'.format(Config.API_URL))
    print('Config.APP_ENV:         {}'.format(Config.APP_ENV))
    

    #use directly dictionary to access all keys 

    ## coming from environment specific file e.g. .env.prod
    print('API_URL:                {}'.format(Config.appConfigs["API_URL"]))


    ## coming from .env file
    print('CURRENY_FORMAT:         {}'.format(Config.appConfigs["CURRENY_FORMAT"]))
    
    
    ## coming from .env.common file
    print('COMMON_APP_VERSION:     {}'.format(Config.appConfigs["COMMON_APP_VERSION"]))
    
    
    #use Config in another module
    ShowAPIkeys_test()


if __name__ == '__main__':
    showconfiguration_test()
