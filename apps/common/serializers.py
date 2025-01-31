from rest_framework import serializers
from . import models


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
            
            
class SellersKworksListSerializers(serializers.ModelSerializer):
        kworks_price = SerializerMethodField()
        
        class Meta():
            model = models.Portfolio
            fields = ['title','cover_image','kworks_price']
                

            