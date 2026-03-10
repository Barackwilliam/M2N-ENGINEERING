from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ============================================================
# SECURITY
# ============================================================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-m2n-engineering-change-this-in-production-2025')

DEBUG = True
ALLOWED_HOSTS = ["www.m2nengineeringcoltd.com","m2nengineeringcoltd.com","localhost","127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://www.m2nengineeringcoltd.com","https://m2nengineeringcoltd.com"]
# ============================================================
# JAZZMIN
# ============================================================
JAZZMIN_SETTINGS = {
    "site_title": "M2N Engineering Admin",
    "site_header": "M2N ENGINEERING",
    "site_brand": "M2N Engineering",
    "site_logo": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Karibu M2N Engineering Management System",
    "copyright": "M2N Engineering Co. Ltd · CRB Class V · BRELA #192412951",
    "search_model": ["website.Service", "website.Project"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "View Website", "url": "/", "new_window": True, "icon": "fas fa-globe"},
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "website",
        "website.SiteSettings",
        "website.SocialMedia",
        "website.HeroSection",
        "website.HeroStat",
        "website.AboutSection",
        "website.AboutFeature",
        "website.Credential",
        "website.ServicesSection",
        "website.Service",
        "website.ServiceFeature",
        "website.ServiceTag",
        "website.ProjectsSection",
        "website.Project",
        "website.ContactSection",
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "website.SiteSettings": "fas fa-cog",
        "website.SocialMedia": "fas fa-share-alt",
        "website.HeroSection": "fas fa-home",
        "website.HeroStat": "fas fa-chart-bar",
        "website.AboutSection": "fas fa-building",
        "website.AboutFeature": "fas fa-list-check",
        "website.Credential": "fas fa-certificate",
        "website.ServicesSection": "fas fa-bolt",
        "website.Service": "fas fa-tools",
        "website.ServiceFeature": "fas fa-check-circle",
        "website.ServiceTag": "fas fa-tags",
        "website.ProjectsSection": "fas fa-project-diagram",
        "website.Project": "fas fa-hard-hat",
        "website.ContactSection": "fas fa-envelope",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}

# ============================================================
# INSTALLED APPS
# ============================================================
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'm2n_engineering.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'm2n_engineering.wsgi.application'

# ============================================================
# DATABASE — Supabase PostgreSQL
# ============================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.hbwbifvbzvkeishhxvtd',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'aws-1-eu-central-1.pooler.supabase.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
        'CONN_MAX_AGE': 600,
    }
}

# ============================================================
# PASSWORD VALIDATION
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================
# INTERNATIONALIZATION
# ============================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC FILES
# ============================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ============================================================
# MEDIA FILES
# ============================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================================================
# SECURITY HEADERS (production only)
# ============================================================
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'