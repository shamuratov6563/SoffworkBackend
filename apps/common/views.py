from rest_framework import generics
from . import models, serializers
from apps.common.serializers import CategorySerializer  


class SellersKworkListAPIView(generics.ListAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.SellersKworkListSerializers



class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'


