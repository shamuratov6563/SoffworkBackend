from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from rest_framework.permissions import AllowAny


from .models import User

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
     


class ConfirmEmailView(APIView):
        def post(self, request, *args, **kwargs):
            user_id = request.data.get('user_id')
            confirmation_code = request.data.get('code')
            try:
                user = User.objects.get(id=str(user_id))
            except (User.DoesNotExist, ValueError):
                return Response({"error": "Foydalanuvchi mavjud emas!"}, status=status.HTTP_400_BAD_REQUEST)
            cached_code = cache.get(f"confirmation_code_{user.email}")

            if not cached_code:
                return Response({"error": "Tasdiqlash kodi muddati o'tgan yoki mavjud emas."})

            if cached_code != confirmation_code:
                return Response({"error": "Tasdiqlash kodi noto'g'ri!"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=user_id)
            user.auth_status = 'confirmed'
            user.save()
            # token jwt generate
            return Response(data=user.tokens(), status=status.HTTP_200_OK)
        

        