import django
from django.conf import settings

def pytest_configure(config):
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "gastos",
        ],

        DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    )
    django.setup()
