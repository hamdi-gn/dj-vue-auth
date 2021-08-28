from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
