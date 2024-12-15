INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',              # Django REST Framework
    'rest_framework.authtoken',    # Token authentication support
    'accounts',                    # Your custom accounts app
]

# Use custom user model
AUTH_USER_MODEL = 'accounts.User'

# Django REST Framework configuration (optional)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,

        
    ],
}
