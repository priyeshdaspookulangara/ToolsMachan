from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
# It's recommended to load this from an environment variable
SECRET_KEY = "your-production-secret-key"

# Configure your production hosts here
ALLOWED_HOSTS = []

# It's highly recommended to use a more robust database for production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "arca_erp",
        "USER": "arca_user",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": "5432",
    }
}
