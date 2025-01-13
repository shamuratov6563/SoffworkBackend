from rest_framework import serializers
from . import models


class HireFreelancerSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.Seller
            fields = "__all__"
            
            
class UserAccountSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.User 
            fields = ('first_name','last_name','bio','image','banner')
            
            
            
class SellerKworksPriceSerializer(serializers.ModelSerializer):
        class Meta():
            model = models.PortfolioPrice
            fields = ('price')        
            
            
class SellersKworksListSerializers(serializers.ModelSerializer):
        kworks_price = SellerKworksPriceSerializer(many=False)
        
        class Meta():
            model = models.Portfolio
            fields = ('title','poster')
                

            