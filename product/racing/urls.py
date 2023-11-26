from django.urls import path
from . import views
from .views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', ProductListAPIView.as_view(), name='product-list-api'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),
]