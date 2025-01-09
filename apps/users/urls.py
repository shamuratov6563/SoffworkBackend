from django.urls import path

from .views import UserView, ConfirmEmailView, UserAPIView

urlpatterns = [
    path('api/v1/user', UserView.as_view()),
    path('api/v1/confirm_email/', ConfirmEmailView.as_view()),
    path('api/v1/list', UserAPIView.as_view()),
]