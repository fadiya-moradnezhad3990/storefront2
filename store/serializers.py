from rest_framework import serializers
from store.models import Product , Collection , Review , Cart , CartItem
from decimal import Decimal


class SimpleProductSerializer(serializers.ModelSerializer):
   class Meta:
      model = Product
      fields=['title' , 'id' , 'unit_price' ]


class ProductSerializer(serializers.ModelSerializer):
  
 class Meta:
     model=Product
     fields=['id','title','slug','description','inventory','unit_price','price_with_tax','collection']
   

 price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

 def calculate_tax(self, product: Product):
    return product.unit_price * Decimal(1.1) 
 



class CollectionSerializer(serializers.ModelSerializer):
  product_count=serializers.IntegerField(read_only=True)
  class Meta:
     model=Collection
     fields=['id','title','product_count']


class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
      Model=Review
      feilds=['id','product','name','description','date']




class CartItemSerializer(serializers.ModelSerializer):
   product=SimpleProductSerializer()
   total_price=serializers.SerializerMethodField()
   def get_total_price(self, cartitem : CartItem):
     return cartitem.quantity *cartitem.product.unit_price
     

   
   class Meta:
      model=CartItem
      fields=['id', 'product' , 'quantity' ,'total_price']
 
class CartSerializer(serializers.ModelSerializer):
   id=serializers.UUIDField(read_only=True)
   items = CartItemSerializer(many=True, read_only=True)
   total_price = serializers.SerializerMethodField()

   def get_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])

   class Meta:
      model=Cart
      fields=['id', 'items' , 'total_price']

class AddCartItemSerializer(serializers.ModelSerializer):
   product_id=serializers.IntegerField()
   class Meta:
      model=CartItem
      fields=['id','product_id' , 'quantity']

   def validated_product_id(self , value):
      if not  Product.objects.filter(pk=value).exists():
         raise serializers.ValidationError("its not a valid ID")
      return value

   def save(self, **kwargs):
             
       cart_id=self.context['cart_id']
       product_id =self.validated_data['product_id']
       quantity=self.validated_data['quantity']

       try:
          cart_item=CartItem.objects.get(cart_id=cart_id , product_id=product_id)
          cart_item.quantity += quantity
          cart_item.save()
          self.instance=cart_item
       except CartItem.DoesNotExist :
          self.instance= CartItem.objects.create(
             cart_id=cart_id,
             product_id=product_id,
             quantity=quantity
          )
          return self.instance

class UpdateCartItemSerializer(serializers.ModelSerialzer):
   class Meta:
      model=CartItem
      fields=['quantity']