from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('shop',views.shop,name="shop"),
    #path('cart',views.cart,name="cart"),
    path('addcart/<int:proid>/', views.addcart, name='addcarts'),
    path('cart/', views.cartitem, name='cartitem'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),

] 