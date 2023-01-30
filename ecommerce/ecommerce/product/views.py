from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Category,Brand, Product
from .serializers import (CategorySerializer, 
BrandSerializere,
 ProductSerializer, 
 ProductLineSerializer
)
from rest_framework.decorators import action

class CategoryView(viewsets.ViewSet):

    """
        A simple Viewset for viewing categories
    """
    
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    serializer_class =  BrandSerializere
    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    """
        A simple Viewset for viewing all products
    """
    queryset = Product.objects.all()
    # lookup_field = "slug"

    def retrieve(self, request, pk=None):
        serializer = ProductSerializer(self.queryset.filter(pk=pk),many=True)

        return Response(serializer.data)

    def list(self,request):
        serializer = ProductSerializer(self.queryset,many=True)
        return Response(serializer.data)
    @action(detail=False,methods=['GET'],url_path=r"category/(?P<category>\w+)/all")
    def list_product_by_category(self,request,category=None):
        """
            An endpoint to return product by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category),many=True)
        return Response(serializer.data)




