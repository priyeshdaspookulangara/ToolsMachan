import os
from django.conf import settings
from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "ComplexPassword123!")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser: {username}")
        User.objects.create_superuser(username=username, password=password, email=email)
    else:
        print(f"Superuser {username} already exists.")

def remove_superuser(apps, schema_editor):
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    if User.objects.filter(username=username).exists():
        print(f"Deleting superuser: {username}")
        User.objects.get(username=username).delete()
    else:
        print(f"Superuser {username} does not exist.")

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=remove_superuser),
    ]
