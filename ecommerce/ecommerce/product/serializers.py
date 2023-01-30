from rest_framework import serializers

from .models import Brand,Category,Product,ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BrandSerializere(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields =  ['name']


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializere()
    category = CategorySerializer()
    product_list = ProductLineSerializer(source='product_line',many=True)
    class Meta:
        model = Product
        fields = '__all__'
