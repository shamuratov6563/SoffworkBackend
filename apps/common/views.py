from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *




class HireFreelancerAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.HireFreelancerSerializer
    
    
class UserAccountAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserAccountSerializer
    
    


class SellersKworkListAPIView(generics.ListAPIView):

    queryset = models.Portfolio.objects.all()
    serializer_class = SellersKworksListSerializers



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
    
    
    
    
#  field for custom permissions


from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer
from .permissions import IsPortfolioOwnerOrSuperuser,IsCommentOwnerOrSuperuser 


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = SellersKworkListSerializers
    permission_classes = [IsAuthenticated, IsPortfolioOwnerOrSuperuser]  # Apply custom permission

    def perform_create(self, serializer):
        # Set the seller to the logged-in user when creating a portfolio
        serializer.save(seller=self.request.user)
        
        
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentOwnerOrSuperuser]  

    def perform_create(self, serializer):
        
        serializer.save(commentator=self.request.user)

