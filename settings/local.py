from .base import *

import os
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.environ.get('LOCAL_SECRET_KEY')
DEBUG = os.environ.get('LOCAL_DEBUG') == 'True'
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"