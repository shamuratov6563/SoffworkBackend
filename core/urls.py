from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.common import views
from pathlib import Path
from path import Path
import os.path




from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/users/', include('users.urls')),
    path('user-account/', views.UserAccountAPIView.as_view()),
    path('kkworks-list/',views.SellersKworksListAPIView.as_view()),
    path('hire-freelancer',views.HireFreelancerAPIView.as_view()),
    
    
]


urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
