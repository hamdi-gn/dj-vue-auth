from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.registration.views import VerifyEmailView


from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet) 

urlpatterns = [
    path(r'^', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
