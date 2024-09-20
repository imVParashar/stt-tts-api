# ######################## #
# #### Configurations #### #
# ######################## #
import os
from os import getenv
from dotenv import load_dotenv

# Loading the env file
load_dotenv('.env')

LOG_LEVEL = 'INFO'
PORT = 5000
HOST = '0.0.0.0'

GROQ_API_KEY = os.environ['GROQ_API_KEY']
DEEPGRAM_API_KEY = os.environ['DEEPGRAM_API_KEY']
