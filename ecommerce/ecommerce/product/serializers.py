from rest_framework import serializers

from .models import (Brand,
                     Category,
                     Product,
                     ProductLine,
                     ProductImage,
                     Attribute, AttributeValue)


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ['category_name']


class BrandSerializere(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['id']


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        exclude = ("id", 'productline')


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["name",]


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta:
        model = AttributeValue
        fields = ['attribute_value', 'attribute']


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)
    attribute_values = AttributeValueSerializer(many=True)

    class Meta:
        model = ProductLine
        # exclude = ['id','is_active','product']
        fields = ['price', 'sku', 'stock_qty', 'order',
                  'product_image', 'attribute_values']


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='name')
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_list = ProductLineSerializer(source='product_line', many=True)

    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'brand_name',
                  'category_name', 'product_list']
