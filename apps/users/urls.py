from django.urls import path

from .views import UserRegisterAPIView, ConfirmEmailView, UserListAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('confirm/', ConfirmEmailView.as_view()),
    path('users-list/', UserListAPIView.as_view()),
]