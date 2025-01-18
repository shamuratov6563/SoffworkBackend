from rest_framework import serializers
from . import models


class SellerKworkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KworkExtraOption
        fields = ('price_of_kwork',)


class SellersKworkListSerializers(serializers.ModelSerializer):
    kwork_price = SellerKworkPriceSerializer(many=False)

    class Meta:
        model = models.Portfolio
        fields = ('title', 'cover_image', 'kwork_price',)
