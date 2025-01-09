from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.users.views import UserView, ConfirmEmailView, UserAPIView

from .schema import swagger_urlpatterns

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/user', UserView.as_view()),
    path('api/v1/confirm_email/', ConfirmEmailView.as_view()),
    path('api/v1/list', UserAPIView.as_view()),

    # JWT auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
