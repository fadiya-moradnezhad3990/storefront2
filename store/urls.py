from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.COllectionViewSet)

products_router= routers.NestedDefaultRouter(router,'products',lookup='product_pk')
products_router.register('reviews', views.ReviewViewSet , basename='product-reviews')
#urlconf
urlpatterns=router.urls


