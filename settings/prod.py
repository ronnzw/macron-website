from .base import *

import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ.get('PROD_SECRET_KEY')
DEBUG = os.environ.get('PROD_DEBUG') == 'True'
ALLOWED_HOSTS = ['www.macronsynergy.co.zw','https://www.macronsynergy.co.zw', 'https://macronsynergy.co.zw', 'macronsynergy.co.zw']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')