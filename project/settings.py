import os
import json
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!

# Verificar si estamos en entorno de desarrollo o producción
DEVELOPMENT_ENVIRONMENT = os.environ.get("DEVELOPMENT_ENVIRONMENT", "False").lower() == "true"

# Configuración de secretos
if DEVELOPMENT_ENVIRONMENT:
    # En entorno de desarrollo, cargar desde secret.json
    with open("secret.json") as f:
        secret = json.loads(f.read())
else:
    # En entorno de producción, usar variables de entorno
    secret = {
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "EMAIL_HOST": os.environ.get("EMAIL_HOST"),
        "EMAIL_HOST_USER": os.environ.get("EMAIL_HOST_USER"),
        "EMAIL_HOST_PASSWORD": os.environ.get("EMAIL_HOST_PASSWORD"),
        "DB_NAME": os.environ.get('DB_NAME'),
        "DB_USER": os.environ.get('DB_USER'),
        "DB_PASSWORD": os.environ.get('DB_PASSWORD'),
        "DB_HOST": os.environ.get('DB_HOST'),
        "DB_PORT": os.environ.get('DB_PORT'),
        # Agrega otras variables según sea necesario
    }

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except KeyError:
        raise ImproperlyConfigured("Set the {} environment variable".format(secret_name))

SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'core',
    'order',
    'proveedores',
    'personal',
    'sucursales',
    'usuarios',
    'ventas',
    'configuraciones'
)

THIRD_PARTY_APPS = (
    'simple_history',
    'guardian',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_tables2',
    'django_filters',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Este es el backend predeterminado de Django.
    'guardian.backends.ObjectPermissionBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # SUCURSALES context_processors: para que este siempre presente el "switch" para cambiar de sucursal (Segun se requiera)
                'core.context_processors.sucursales',
                # SIDEBAR context_processors: para que se renderizen las opciones segun los permisos (Segun se requiera)
                'core.context_processors.sidebar',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Configuración para el uso de base de datos en Heroku
if DEVELOPMENT_ENVIRONMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_secret('DB_NAME'),
            'USER': get_secret('DB_USER'),
            'PASSWORD': get_secret('DB_PASSWORD'),
            'HOST': get_secret('DB_HOST'),
            'PORT': get_secret('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#REDIRECT

LOGIN_URL = 'usuarios/accounts/login/'
LOGIN_REDIRECT_URL = 'usuario/accounts/login/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "static/"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Email settings for sending emails
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'oscarvargas3873@gmail.com'
EMAIL_HOST_PASSWORD = 'zumh xzqx vido xjct '
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


AUTH_USER_MODEL = 'usuarios.UsuarioPersonalizado'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"