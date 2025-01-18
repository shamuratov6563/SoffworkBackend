from django.urls import path
from apps.common import views


urlpatterns = [
    path('kworks/', views.SellersKworkListAPIView.as_view()),
]