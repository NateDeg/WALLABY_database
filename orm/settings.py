import os

# ---------------------------------------------------------------------------------------
# Application

INSTALLED_APPS = [
    "orm",
    "source_finding"
]

USE_TZ = False

# ---------------------------------------------------------------------------------------
# Database

DATABASE_ENGINE = os.environ.get(
    'DATABASE_ENGINE',
    'django.db.backends.postgresql'
)
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER', 'admin')
DATABASE_PASS = os.environ.get('DATABASE_PASS')

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'OPTIONS': {
            'options': '-c search_path=public,wallaby'
        },
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASS,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
}
