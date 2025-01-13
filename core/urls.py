from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.common import views
from pathlib import Path
from path import Path
import os.path





from .schema import swagger_urlpatterns

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    # path('api/users/', include('users.urls')),
    path('user-account/', views.UserAccountAPIView.as_view()),
    path('kkworks-list/',views.SellersKworksListAPIView.as_view()),
    path('hire-freelancer',views.HireFreelancerAPIView.as_view()),
    
    
=======
    path('auth/', include('apps.users.urls')),

    # JWT auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

>>>>>>> ed0023e70e6e62cda9ef0e814b79ce2b305eedd6
]


urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
