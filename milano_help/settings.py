"""
Django settings for milano_help project.
"""

from pathlib import Path

# --- Percorsi ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Sicurezza ---
SECRET_KEY = 'django-insecure-uh@l67(=17&z_0)qa6s5b1n-nrn_q#98na5px#t4dhe4a!wp%g'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'milanohelp2.onrender.com']

# --- App installate ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # App progetto
    'core',
]

SITE_ID = 1  # 1 o 2 in base al tuo db

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --- URL principale ---
ROOT_URLCONF = 'milano_help.urls'

# --- Template ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # richiesto da allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION = 'milano_help.wsgi.application'

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --- Internazionalizzazione ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static e media ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # se usi cartella static
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Login/Logout ---
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# --- Backends autenticazione ---
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth
)

# --- Allauth settings aggiornati ---
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # login via email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# --- Email backend (per sviluppo locale) ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
