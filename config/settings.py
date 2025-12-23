import os
import sys
import environ
from pathlib import Path
from datetime import timedelta
from django.urls import reverse_lazy

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, 'apps'))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


DJANGO_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'unfold.contrib.guardian',
    'unfold.contrib.simple_history',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    # 'corsheaders', # Uncomment if corsheaders is installed/needed
]

LOCAL_APPS = [
    'apps.profiles.account',
    'apps.profiles.staff',

    'apps.directory.area',
    'apps.directory.product',
    'apps.directory.warebank',
    'apps.directory.template',
    'apps.directory.delivery',
    'apps.directory.measurement',
    'apps.directory.purchase',
    'apps.directory.organization',

    'apps.documents.analysis',
    'apps.documents.appeal',
    'apps.documents.commercial',
    'apps.documents.plan',
    'apps.documents.purchase',
    'apps.documents.sales.orders',
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware', # Uncomment if corsheaders is installed/needed
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT')
    } if env.str('DB_ENGINE') == 'postgresql' else {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'uz-Uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'v3/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'profil_account.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=30),
}

UNFOLD = {
    "SITE_TITLE": "EKomplektasiya | Admin",
    "SITE_HEADER": "EKomplektasiya",
    "SHOW_HISTORY": True,
    "SITE_URL": "/",
    # "SITE_ICON": {
    #     "light": lambda request: STATIC_URL + "img/logo.svg",  # light mode
    #     "dark": lambda request: STATIC_URL + "img/logo.svg",  # dark mode
    # },
    "DASHBOARD_CALLBACK": "config.dashboard.dashboard_callback",
    "ENVIRONMENT": "apps.core.utils.environment_callback",
    "LOGIN": {
        "title": "EKomplektasiya Tizimi",
        "description": "Xush kelibsiz! Tizimga kirish uchun login va parolingizni kiriting.",
        "show_title": True,
        "show_description": True,
    },
    "COLORS": {
        "primary": {
            "50": "239 246 255",
            "100": "219 234 254",
            "200": "191 219 254",
            "300": "147 197 253",
            "400": "96 165 250",
            "500": "59 130 246",
            "600": "37 99 235",
            "700": "29 78 216",
            "800": "30 64 175",
            "900": "30 58 138",
            "950": "23 37 84",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Hujjatlar (Documents)",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Buyurtmalar",
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                    },
                    {
                        "title": "Tijorat takliflari",
                        "icon": "description",
                        "link": reverse_lazy("admin:commercial_commercial_changelist"),
                    },
                    {
                        "title": "Narx tahlillari",
                        "icon": "analytics",
                        "link": reverse_lazy("admin:analysis_priceanalysis_changelist"),
                    },
                    {
                        "title": "Yillik Reja",
                        "icon": "calendar_today",
                        "link": reverse_lazy("admin:plan_annualplan_changelist"),
                    },
                    {
                        "title": "Apelyatsiya Xatlari",
                        "icon": "gavel",
                        "link": reverse_lazy("admin:appeal_appealletter_changelist"),
                    },
                    {
                        "title": "Xaridlar (Bank)",
                        "icon": "account_balance_wallet",
                        "link": reverse_lazy("admin:doc_purchase_purchasetypebank_changelist"), 
                    },
                ],
            },
            {
                "title": "Ma'lumotnomalar (Directory)",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Mahsulotlar",
                        "icon": "inventory_2",
                        "link": reverse_lazy("admin:product_productmodel_changelist"), 
                    },
                     {
                        "title": "Mahsulot Turlari",
                        "icon": "category",
                        "link": reverse_lazy("admin:product_producttype_changelist"),
                    },
                    {
                        "title": "Kategoriyalar",
                        "icon": "class",
                        "link": reverse_lazy("admin:measurement_category_changelist"),
                    },
                    {
                        "title": "O'lchov Birliklari",
                        "icon": "straighten",
                        "link": reverse_lazy("admin:measurement_unit_changelist"),
                    },
                    {
                        "title": "Hududlar",
                        "icon": "location_on",
                        "link": reverse_lazy("admin:area_region_changelist"),
                    },
                    {
                        "title": "Tashkilotlar",
                        "icon": "business",
                        "link": reverse_lazy("admin:organization_department_changelist"),
                    },
                     {
                        "title": "Yetkazib berish",
                        "icon": "local_shipping",
                        "link": reverse_lazy("admin:delivery_deliverycondition_changelist"),
                    },
                     {
                        "title": "Banklar & Omborlar",
                        "icon": "store",
                        "link": reverse_lazy("admin:warebank_bank_changelist"),
                    },
                ],
            },
            {
                "title": "Foydalanuvchilar (Users)",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Xodimlar",
                        "icon": "badge",
                        "link": reverse_lazy("admin:staff_employee_changelist"),
                    },
                    {
                        "title": "Tizim foydalanuvchilari",
                        "icon": "person",
                        "link": reverse_lazy("admin:profil_account_user_changelist"),
                    },
                    {
                        "title": "Guruhlar",
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
