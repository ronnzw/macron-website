from .base import *

import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ.get('PROD_SECRET_KEY')
DEBUG = os.environ.get('PROD_DEBUG') == 'True'
ALLOWED_HOSTS = ['www.macronsynergy.co.zw','https://www.macronsynergy.co.zw']