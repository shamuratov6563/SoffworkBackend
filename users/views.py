from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

from .models import User

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConfirmEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        confirmation_code = request.data.get('confirmation_code')

        try:
            # Foydalanuvchini topish
            user = User.objects.get(email=email)
            
            # Cache-dan tasdiqlash kodini olish
            cached_code = cache.get(f"confirmation_code_{email}")
            
            if not cached_code:
                return Response({"error": "Tasdiqlash kodi muddati o'tgan yoki mavjud emas!"}, status=status.HTTP_400_BAD_REQUEST)

            # Kodni tekshirish
            if cached_code == confirmation_code:
                user.email_confirmed = True
                user.save()
                cache.delete(f"confirmation_code_{email}")  # Kodni tekshirishdan so'ng, cache dan olib tashlash
                return Response({"message": "Email tasdiqlandi!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Tasdiqlash kodi noto'g'ri!"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)