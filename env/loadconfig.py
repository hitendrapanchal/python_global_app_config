from os import environ,path
from dotenv import  dotenv_values
import os

dotenv_path="/env"
#Load Configuration :loadConfiguration() need to be invoked in app.py 
#The function dotenv_values works more or less the same way as load_dotenv, except it doesn't touch the environment, it just returns a dict with the values parsed from the .env file.

#This appConfigs  global variable will be used in config.py

def loadConfiguration(APP_ENV=None):
    print('loadConfiguration started')
    #APP_ENV could be dev/qa/uat/prod
    current_env=''
    
    #if pass from calling function
    if APP_ENV:
        current_env=APP_ENV
        print("APP_ENV is passed as argument to loadConfiguration()")
    #if pass from python command line or already set in operating system environment variable
    elif os.environ.get("APP_ENV"):
        current_env=environ.get("APP_ENV")
        print("APP_ENV:{} is received from operating system environment in loadConfiguration()".format(current_env))
    else:
        #default to dev
        current_env='dev'
        print("APP_ENV is not received from anywhere hence it is set to default with dev in loadConfiguration()")
    
    print('loadConfiguration completed for environment:',current_env)
    return loadfromFile(current_env)

    
def loadfromFile(current_env):
    print('loadfromFile started for environment:', current_env)
    # Load variables from .env with ** destructuring
    basedir = path.abspath(path.dirname(__file__))
    
    dot_env_file_path=path.join(basedir, ".env") 
    env_file_path=path.join(basedir, ".env.") + current_env
    common_file_path=path.join(basedir, ".env.") + "common"

    appConfigs={
            **dotenv_values(dot_env_file_path),   #This will populate in dict first  e.g .env
            **dotenv_values(common_file_path),   #This will populate in dict first  e.g .env.common
            **dotenv_values(env_file_path),      #This will override and take priority in case of same key   e.g .env.dev
            **os.environ                         #This will override and take higher precedence.
            }

    
    print('loadfromFile completed for environment:',current_env)
    return appConfigs

        
    
    
        
    
        
    