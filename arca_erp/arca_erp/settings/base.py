
from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "drf_yasg",

    # Local apps
    'apps.core.admin_core.apps.AdminCoreConfig',
    'apps.core.data_hub.apps.DataHubConfig',
    'apps.core.event_core.apps.EventCoreConfig',
    'apps.core.service_bridge.apps.ServiceBridgeConfig',
    'apps.core.auth_core.apps.AuthCoreConfig',
    'apps.business.asset_care.apps.AssetCareConfig',
    'apps.business.cost_mgmt.apps.CostMgmtConfig',
    'apps.business.finance_core.apps.FinanceCoreConfig',
    'apps.business.material_core.apps.MaterialCoreConfig',
    'apps.business.order_mgmt.apps.OrderMgmtConfig',
    'apps.business.pay_link.apps.PayLinkConfig',
    'apps.business.prod_core.apps.ProdCoreConfig',
    'apps.business.quality_core.apps.QualityCoreConfig',
    'apps.business.tax_core.apps.TaxCoreConfig',
    'apps.business.warehouse_x.apps.WarehouseXConfig',
    'apps.hr.org_core.apps.OrgCoreConfig',
    'apps.hr.people_ops.apps.PeopleOpsConfig',
    'apps.hr.talent_hub.apps.TalentHubConfig',
    'apps.retail.checkout.apps.CheckoutConfig',
    'apps.retail.customer_360.apps.Customer360Config',
    'apps.retail.lead_ops.apps.LeadOpsConfig',
    'apps.retail.loyalty_plus.apps.LoyaltyPlusConfig',
    'apps.retail.price_core.apps.PriceCoreConfig',
    'apps.retail.promo_core.apps.PromoCoreConfig',
    'apps.retail.retail_hub.apps.RetailHubConfig',
    'apps.retail.retail_pos.apps.RetailPosConfig',
    'apps.retail.service_desk.apps.ServiceDeskConfig',
    'apps.retail.sync_hub.apps.SyncHubConfig',
    'apps.scm.fleet_ops.apps.FleetOpsConfig',
    'apps.scm.purchase_hub.apps.PurchaseHubConfig',
    'apps.scm.supply_core.apps.SupplyCoreConfig',
    'apps.analytics.compliance_core.apps.ComplianceCoreConfig',
    'apps.analytics.data_insights.apps.DataInsightsConfig',
    'apps.analytics.forecast_x.apps.ForecastXConfig',
    'apps.analytics.trace_core.apps.TraceCoreConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "arca_erp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "arca_erp.wsgi.application"
ASGI_APPLICATION = "arca_erp.asgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Simple JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True # For development only

# Celery
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Swagger
SWAGGER_SETTINGS = {
    'LOGIN_URL': '/api/auth/session/login/',
    'LOGOUT_URL': '/api/auth/session/logout/',
}

JAZZMIN_SETTINGS = {
    "site_title": "ARCA ERP Admin",
    "site_header": "ARCA ERP",
    "site_brand": "ARCA ERP",
    "welcome_sign": "Welcome to ARCA ERP",
    "copyright": "ARCA Systems Ltd.",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Finance", "url": "/admin/finance_core/", "permissions": ["auth.view_user"]},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "finance_core", "people_ops", "order_mgmt", "material_core"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "finance_core.account": "fas fa-university",
        "finance_core.journalentry": "fas fa-book",
        "finance_core.transaction": "fas fa-exchange-alt",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "show_ui_builder": True
}
