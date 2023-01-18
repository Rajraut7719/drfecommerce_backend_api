# Packeages

Django==3.2.16
djangorestframework==3.14.0
python-dotenv==0.21.0
pytest==7.2.1
pytest-django==4.5.2

# Commands
django-admin startproject ecommerce

python manage.py runserver

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
