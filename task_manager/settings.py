# task_manager/settings.py  — ПОЛНЫЙ ФАЙЛ

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv # <-- Добавили импорт ainiddin
# [ОБЩАЯ БАЗА] Базовые пути проекта
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR.parent / ".env"
load_dotenv(env_path)
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True
ALLOWED_HOSTS = ["*"]


# ── Приложения ────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    # Стандартные приложения Django (НЕ УДАЛЯТЬ!)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # [РОЛЬ 1 - Безопасность] Пакеты для API и авторизации
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    
    # [РОЛЬ 3 - Интеграции] Пакет для фоновых задач (рассылок)
    "django_apscheduler",
    
    # [РОЛЬ 2 - Логика] Наше главное приложение (если будут новые, Роль 2 добавит их сюда)
    "core",
]
 
# [ОБЩАЯ БАЗА] Слой промежуточной обработки (трогать редко)
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "task_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "task_manager.wsgi.application"

# ── База данных ───────────────────────────────────────────────────────────
# [РОЛЬ 2 - Логика] Управление подключением к БД
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ── Кастомная модель пользователя ─────────────────────────────────────────
# [РОЛЬ 1 - Безопасность] Указание на новую модель юзера
AUTH_USER_MODEL = "core.CustomUser"

# ── Валидация паролей ─────────────────────────────────────────────────────
# [РОЛЬ 1 - Безопасность] Правила сложности паролей
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ── Локализация ───────────────────────────────────────────────────────────
LANGUAGE_CODE = "ru-ru"
# [РОЛЬ 3 - Интеграции] ВАЖНО: часовой пояс влияет на то, когда отправляются email-уведомления!
TIME_ZONE     = "Asia/Almaty"
USE_I18N      = True
USE_TZ        = True

# ── Статика ───────────────────────────────────────────────────────────────
# [ОБЩАЯ БАЗА]
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ── DRF + JWT ─────────────────────────────────────────────────────────────
# [РОЛЬ 1 - Безопасность] Глобальные настройки доступа и токенов
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME":    timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME":   timedelta(days=7),
    "ROTATE_REFRESH_TOKENS":    True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES":        ("Bearer",),
}

# ── Email ───────────────────────────────────────
EMAIL_BACKEND      = "django.core.mail.backends.smtp.EmailBackend" # Заменить на smtp в проде
EMAIL_HOST         = "smtp.gmail.com"
EMAIL_PORT         = 465
EMAIL_USE_TLS      = False
EMAIL_USE_SSL       = True
# EMAIL_HOST_USER    = "taskflow872@gmail.com"
# EMAIL_HOST_PASSWORD = "0584 5671"   # код от гугл нужно создать env перенести этот пароль туда и использовать python-dotenv
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ── APScheduler ───────────────────────────────────────────────────────────
# [РОЛЬ 3 - Интеграции] Настройки планировщика задач (для рассылки писем по дедлайнам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25