# ######################## #
# #### Configurations #### #
# ######################## #

from os import getenv
from dotenv import load_dotenv

# Loading the env file
load_dotenv('stt-tts-api.env')

LOG_LEVEL = 'INFO'
PORT = 5000
HOST = '0.0.0.0'
