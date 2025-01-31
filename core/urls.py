from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.common import views
from django.urls import path

from .schema import swagger_urlpatterns

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

<<<<<<< HEAD
    # path('api/users/', include('users.urls')),
    path('user-account/<int:pk>/', views.UserAccountAPIView.as_view()),
    path('kworks-list/<int:pk>/',views.SellersKworksListAPIView.as_view()),
    path('hire-freelancer/<int:pk>/',views.HireFreelancerAPIView.as_view()),
    
    
=======
    path('api/v1/common/', include('apps.common.urls')),


>>>>>>> 86749fad1f7d3b036ccb7a3e74843ac3d4445fbe

    path('auth/', include('apps.users.urls')),


    # JWT auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
