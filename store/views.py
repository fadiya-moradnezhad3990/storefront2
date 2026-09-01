from django.shortcuts import get_object_or_404
from django.db.models import Count , Exists
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product , Collection , Review
from .serializers import ProductSerializer , CollectionSerializer ,ReviewSerializer


class ProductViewSet(ModelViewSet):
  
  queryset=Product.objects.all()
  serializer_class=ProductSerializer

  def get_serializer_context(self):
    return {'request':self.request}
  
   
  def destroy(self, request, *args, **kwargs):
    product=self.get_object()

    if product.orderitem_set.exists() > 0 :
      return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    return super().destroy(request, *args, **kwargs)
 


class CollectionViewSet(ModelViewSet):
  queryset=Collection.objects.annotate(product_count=Count('product'))
  serializer_class=CollectionSerializer

  def destroy(self, request, *args, **kwargs):
    collection=self.get_object()

    if collection.product.exists() >0:
      return Response({'error':'This Collection cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
  queryset=Review.objects.all()
  serializer_class= ReviewSerializer  