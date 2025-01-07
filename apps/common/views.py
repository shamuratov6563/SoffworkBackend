from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
# Create your views here.
class Digital_serviceView(APIView):
    queryset=Digital_service.objects.all()
    serializer_class=Digital_serviceSerializer