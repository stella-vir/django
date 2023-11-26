from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse


def home(request):
    # Retrieve and prepare data from your 'racing' app or any other relevant data source
    # For example:
    data = {
        'message': 'from Django to React',
        'product': 'Electric Motor'
    }
    return JsonResponse(data)

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
