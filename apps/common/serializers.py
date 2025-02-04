from rest_framework import serializers
from . import models
from .models import Category
   



class HireFreelancerSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.Seller
            fields = "__all__"
            
            
class UserAccountSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.User 
            fields = ('name','user_info','user_photo','user_banner',)
            
            
            
class SellerKworksPriceSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.KworkExtraOption
            fields = ('price_of_kwork',)        
            



class SellerKworkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KworkExtraOption
        fields = ('price_of_kwork',)

    def validate_price_of_kwork(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

class SellersKworkListSerializers(serializers.ModelSerializer):
    kwork_price = serializers.SerializerMethodField()
    kworks_likes = serializers.SerializerMethodField()

    class Meta:
        model = models.Portfolio
        fields = ('title', 'cover_image', 'kwork_price',)

    def get_kwork_price(self, obj):
        return obj.kwork_price.price_of_kwork if obj.kwork_price else None



class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'image', 'parent', 'order')

    def get_parent(self, obj):
        if obj.parent:
            return CategorySerializer(obj.parent).data
        return None


class SellerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SellerSkill
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'commentator', 'body', 'reply_to', 'kwork')



class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceType
        fields = '__all__'

class KworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kwork
        fields = '__all__'

class KworkFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KworkFeedback
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'

class PortfolioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioFile
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'

class KworkFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KworkFile
        fields = '__all__'
        
        
        
        
            
class SellersKworksListSerializers(serializers.ModelSerializer):
        likes = serializers.SerializerMethodField()
    
        class Meta():
            model = models.Portfolio
            fields = ['title','cover_image','kworks_price','likes',]
        
        def get_likes(self, obj):
            return obj.likes.count()