import os
import sys
from pathlib import Path

### Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

BOOTSTRAP5_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "django_bootstrap5"))
if BOOTSTRAP5_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP5_FOLDER)

### Quick-start development settings - unsuitable for production
### See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

### SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gut+seym7@^5p8p_pb+0qj9&r7r%j*2r#gr%e+!85e6bq2fm$c'

### SECURITY WARNING: don't run with debug turned on in production!
### DEBUG = True                                                               ### 2024/11/20 COMMENT OUT
DEBUG = False                                                                  ### 2024/11/20 ADD

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    'http://suigaidemo.river.or.jp',
    'https://suigaidemo.river.or.jp',
    'http://35.76.231.190',
    'https://35.76.231.190',
    'http://localhost',
    'https://localhost',
    'http://suigai-dev-alb-35061489.ap-northeast-1.elb.amazonaws.com',
    'https://suigai-dev-alb-35061489.ap-northeast-1.elb.amazonaws.com']        ### 2023/11/20 ADD

INSTALLED_APPS = [
    'django_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ### Message Queue Applications
    'MessageQueue.apps.MessageQueueConfig',
    
    ### Common Applications
    'P0000Common.apps.P0000CommonConfig',
    'P0100Login.apps.P0100LoginConfig',

    ### File Applications
    'P0110City.apps.P0110CityConfig',
    'P0120Ken.apps.P0120KenConfig',
    'P0130Manage.apps.P0130ManageConfig',
    'P0140Weather.apps.P0140WeatherConfig',
    'P0150Truncate.apps.P0150TruncateConfig',
    
    ### Excel Applications
    'P0200Download.apps.P0200DownloadConfig',
    
    ### Online Applications
    'P0400Online.apps.P0400OnlineConfig',

    ### Suigai Map Applications
    'P0500GUI.apps.P0500GUIConfig',                                            ### Kimura added this line on 2024/01/23, to include a new webpage.

    ### EStat Applications
    'P0700EStat.apps.P0700EStatConfig',                                        ### This URL is not planned to be released in the 2024 release.
    
    'P0900Action.apps.P0900ActionConfig',                                      ### 2024/11/14 download_IPP_ACT_90.py等のcommandを動かすため、コメントを外した。
]

### These items in your MIDDLEWARE setting:
### 1. SessionMiddleware manages sessions across request.
### 2. AuthenticationMiddleware associates users with requests using sessions.
### With these settings in place, running the command manage.py migrate
### creates the necessary database tables for auth related models and
### permissions for any models defined in your installed apps.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'suigai_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        ### 'DIRS': [],                                                        ### COMMENT OUT 2024/01/23 KIMURA
        'DIRS': [os.path.join(BASE_DIR, 'P0500GUI', 'templates')],             ### ADD 2024/01/23 KIMURA
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'suigai_website.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'suigai_web',
        'USER': 'frics',
        'PASSWORD': 'frics',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

### Password validation
### https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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

### Internationalization
### https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

### Static files (CSS, JavaScript, Images)
### https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    ### os.path.join(BASE_DIR, 'suigai', 'lib'),                               ### ADD 2024/01/23 KIMURA ### COMMENT OUT 2024/07/24 OKADA
    os.path.join(BASE_DIR, 'static', 'suigai', 'lib'),                         ### ADD 2024/07/24 OKADA
)

### Default primary key field type
### https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOG_BASE_DIR = os.path.join("/var", "log")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(asctime)s [%(levelname)s] %(message)s"}},
    "handlers": {
        "info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "info.log"),
            "formatter": "simple",
        }, 
        "warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "warning.log"),
            "formatter": "simple",
        }, 
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "error.log"),
            "formatter": "simple",
        },
    },
}

### Settings for django-bootstrap5
BOOTSTRAP5 = {
    "error_css_class": "django_bootstrap5-error",
    "required_css_class": "django_bootstrap5-required",
    "javascript_in_head": True,
}

### AUTH_USER_MODEL = 'P0100Login.MyUser'
### See Python Django開発入門, P224
### django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定する。
SITE_ID=1

### See Python Django開発入門, P224
### 認証バックエンド（認証を検証するクラス）を２つ設定する。
### Djangoは認証バックエンドを複数設定できる。
### 具体的には、AUTHENTICATION_BACKENDSリストに設定した認証バックエンドを順に認証できるまで試行する。
### AUTHENTICATION_BACKENDS = (
###     ### 一般ユーザ用（メールアドレス認証）
###     'allauth.account.auth_backends.AuthenticationBackend',
###     ### 管理サイト用（ユーザ名認証）
###     'django.contrib.auth.backends.ModelBackend',
### )
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
### メールアドレス認証に変更する
### ACCOUNT_AUTHENTICATION_METHOD = 'email'
### ACCOUNT_USERNAME_REQUIRED = False
### サインアップにメールアドレス確認をはさむように設定する
### ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
### ACCOUNT_EMAIL_REQUIRED = True
### ログイン、ログアウト後の遷移先を設定する
### LOGIN_REDIRECT_URL = 'diary:index'
### ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
### ログアウトリンクのクリックでログアウトするように設定する
### ACCOUNT_LOGOUT_ON_GET = True
### django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにするように設定する
### ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
### デフォルトのメール送信元を設定する
### DEFAULT_FROM_EMAIL = os.environ.get('FROM_EMAIL')

### X_FRAME_OPTIONS = 'SAMEORIGIN'                                             ### ADD 2023/02/07 ### COMMENT OUT 2023/11/09 FOR TEMPORARY TEST

MEDIA_ROOT = os.path.join(BASE_DIR, 'temp_images')                             ### ADD 2024/01/23 KIMURA
MEDIA_URL = '/media/'                                                          ### ADD 2024/01/23 KIMURA
