from rest_framework import serializers
from . import models
from .models import Category
   



class SellerKworkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KworkExtraOption
        fields = ('price_of_kwork',)


class SellersKworkListSerializers(serializers.ModelSerializer):
    kwork_price = SellerKworkPriceSerializer(many=False)

    class Meta:
        model = models.Portfolio
        fields = ('title', 'cover_image', 'kwork_price',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'image', 'parent', 'order')





