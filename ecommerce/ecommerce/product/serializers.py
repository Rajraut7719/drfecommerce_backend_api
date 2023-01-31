from rest_framework import serializers

from .models import Brand,Category,Product,ProductLine


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ['category_name']

class BrandSerializere(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['id']


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ['id','is_active','product']

class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source ='name')
    brand_name = serializers.CharField(source ='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_list = ProductLineSerializer(source='product_line',many=True)
    class Meta:
        model = Product
        fields = ['product_name','slug','brand_name','category_name','product_list']
