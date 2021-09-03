
import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_vue_auth.settings')

application = Cling(get_wsgi_application())
