"""
secret key to the project.

https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""

import os

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '(4xc5@kw^aevy60mk+0@2snj=4077t!$=tw6jjphomd4h!i%no'
)
