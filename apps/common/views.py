from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *



<<<<<<< HEAD

class HireFreelancerAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.HireFreelancerSerializer
    
    
class UserAccountAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserAccountSerializer
    
    
class SellersKworksListAPIView(generics.RetrieveUpdateAPIView):
=======
class SellersKworkListAPIView(generics.ListAPIView):
>>>>>>> 86749fad1f7d3b036ccb7a3e74843ac3d4445fbe
    queryset = models.Portfolio.objects.all()
    serializer_class = SellersKworkListSerializers



class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class SellerSkillListCreateView(generics.ListCreateAPIView):
    queryset = SellerSkill.objects.all()
    serializer_class = SellerSkillSerializer
    permission_classes = [IsAuthenticated]

class KworkListCreateView(generics.ListCreateAPIView):
    queryset = Kwork.objects.all()
    serializer_class = KworkSerializer
    permission_classes = [IsAuthenticated]

class KworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kwork.objects.all()
    serializer_class = KworkSerializer
    permission_classes = [IsAuthenticated]

class PortfolioListCreateView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = SellersKworkListSerializers
    permission_classes = [IsAuthenticated]

class PortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = SellersKworkListSerializers
    permission_classes = [IsAuthenticated]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class KworkFileListCreateView(generics.ListCreateAPIView):
    queryset = KworkFile.objects.all()
    serializer_class = KworkFileSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class KworkViewSet(viewsets.ModelViewSet):
    queryset = Kwork.objects.all()
    serializer_class = KworkSerializer
    permission_classes = [IsAuthenticated]

class KworkViewSet(viewsets.ModelViewSet):
    queryset = Kwork.objects.all()
    serializer_class = KworkSerializer
    permission_classes = [IsAuthenticated]
