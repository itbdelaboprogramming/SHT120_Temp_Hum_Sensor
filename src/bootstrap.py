import os
from dotenv import load_dotenv

env_loaded = False
DEVICE_ADDR,DEVICE_DEBUG,PORT_NAME = None, None, None
def load_env():
    global env_loaded,DEVICE_ADDR,DEVICE_DEBUG,PORT_NAME

    if not env_loaded:
        dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        env_loaded = True
        DEVICE_ADDR = int(os.getenv('DEVICE_ADDR'))
        PORT_NAME = str(os.getenv('PORT_NAME'))

load_env()

if __name__ == "__main__":
    print(DEVICE_ADDR,DEVICE_DEBUG,PORT_NAME)   
