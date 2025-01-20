from django.urls import path
from apps.common import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('kworks/', views.SellersKworkListAPIView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)