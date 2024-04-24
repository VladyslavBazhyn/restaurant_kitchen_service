import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_kitchen_service.restaurant_kitchen_service.settings")

application = get_wsgi_application()
