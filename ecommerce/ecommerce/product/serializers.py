from rest_framework import serializers

from .models import Brand,Category,Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BrandSerializere(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields =  ['name']

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializere()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'