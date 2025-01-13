from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from apps.common import views
from django.urls import path



from .schema import swagger_urlpatterns

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path("admin/", admin.site.urls),

    # path('api/users/', include('users.urls')),
    path('user-account/', views.UserAccountAPIView.as_view()),
    path('kkworks-list/',views.SellersKworksListAPIView.as_view()),
    path('hire-freelancer',views.HireFreelancerAPIView.as_view()),
    
    

    path('auth/', include('apps.users.urls')),

    # JWT auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
