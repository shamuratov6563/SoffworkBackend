from rest_framework import generics
from . import models, serializers


class SellersKworkListAPIView(generics.ListAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.SellersKworkListSerializers
