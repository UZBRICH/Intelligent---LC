import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_center.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = 'admin'
EMAIL = 'richuzb13@gmail.com'
PASSWORD = os.environ.get('ADMIN_PASSWORD')

if not User.objects.filter(username=USERNAME).exists():
    print(f"Creating superuser {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully!")
else:
    print(f"Superuser {USERNAME} already exists.")