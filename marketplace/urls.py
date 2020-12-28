from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "product"


urlpatterns = [
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail,name='cart_detail'),
    path("e-market/", views.EmarketView.as_view(), name="e-market"),

    path('add-product/', views.AddProductView.as_view(), name="add-product"),
    path('my-shop/', views.MyShopProductView.as_view(), name="my-shop"),
    path('update-product/', views.UpdateProductView.as_view(), name="update-product"),
    path('edit-product/<int:pk>', views.EditProductView.as_view(), name="edit-product"),
    path('delete-product/<int:pk>', views.DeleteProductView.as_view(), name="delete-product"),
    path('details-product/<int:pk>', views.DetailProductView.as_view(), name="details-product"),
    path('seller-contact/<int:pk>', views.SellerContactView.as_view(), name="seller-contact"),
    path("product-by-category/<int:pk>", views.ProductByCategory.as_view(), name="product-by-category"),
    path('order-submit', views.OrderSubmit.as_view(), name="order-submit"),
    path('product-search', views.ProductSearchView.as_view(), name="product-search"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)