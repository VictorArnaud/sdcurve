"""
Django Rest Framework

http://www.django-rest-framework.org/
http://getblimp.github.io/django-rest-framework-jwt/
"""

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False
}
