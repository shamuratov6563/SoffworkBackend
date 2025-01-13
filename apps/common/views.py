from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from . import models, serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.views import Response




class HireFreelancerAPIView(generics.ListAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.HireFreelancerSerializer
    
    
class UserAccountAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserAccountSerializer
    
    
class SellersKworksListAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.SellersKworksListSerializers
    
    
    