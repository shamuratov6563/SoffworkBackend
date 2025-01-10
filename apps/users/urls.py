from django.urls import path

from .views import UserRegisterAPIView, ConfirmEmailView, UserListAPIView

urlpatterns = [
    path('api/v1/register/', UserRegisterAPIView.as_view()),
    path('api/v1/confirm/', ConfirmEmailView.as_view()),
    path('api/v1/list/', UserListAPIView.as_view()),
]