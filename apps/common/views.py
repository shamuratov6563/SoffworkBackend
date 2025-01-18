from rest_framework import generics
from . import models, serializers


class UserAccountAPIView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserAccountSerializer


class SellersKworkListAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.SellersKworkListSerializers
