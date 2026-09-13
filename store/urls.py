from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet , basename='prodcuts')
router.register('collections', views.CollectionViewSet)
router.register('carts',views.CartViewSet )


products_router= routers.NestedDefaultRouter(router,'products',lookup='product_pk')
products_router.register('reviews', views.ReviewViewSet , basename='product-reviews')

cart_router=routers.NestedDefaultRouter(router , 'carts' , lookup='cart_pk')
cart_router.register('items',views.CartItemViewSet , basename='cart_items')
#urlconf
urlpatterns=router.urls +products_router.urls +cart_router.urls


