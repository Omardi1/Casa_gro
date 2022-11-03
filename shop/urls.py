from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import cart_add, cart_detail, cart_remove
from shop.views import Product_detail,  index,  ProductList, ProductDetail

urlpatterns = [
    path('', index, name='index'),
    path("shop/", ProductList.as_view(), name="product-list"),
     path("shop/<slug:slug>/details/",
         ProductDetail.as_view(), name="product-details"),
    path('Product/<str:slug>/', Product_detail, name="product"),
    path("cart_detail", cart_detail, name="cart_detail"),
    path("add/<str:slug>/", cart_add, name="cart_add"),
    path("remove/<int:product_id>/", cart_remove, name="cart_remove"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)