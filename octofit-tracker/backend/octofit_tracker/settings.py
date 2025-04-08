# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS = INSTALLED_APPS if 'INSTALLED_APPS' in locals() else []
INSTALLED_APPS += ['corsheaders']

MIDDLEWARE = MIDDLEWARE if 'MIDDLEWARE' in locals() else []
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']