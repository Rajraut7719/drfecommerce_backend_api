from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Category,Brand, Product
from .serializers import CategorySerializer, BrandSerializere, ProductSerializer


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
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)


