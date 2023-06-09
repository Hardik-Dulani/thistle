
from django.urls import path,include
from main import views

urlpatterns = [path('',views.index),
               path('logout', views.handelLogout, name="handleLogout"),
               path('accounts/',include('allauth.urls')),
               path('products/<int:myid>',views.productview,name="ProductView"),
               path('orders/order-id:gikud781<myid>',views.orderview,name="orderView"),
               path('categories/<category>',views.categoryview,name="orderView"),
               path('cart/',views.cart,name='cart'),
               path('checkout/',views.checkout,name='checkout'),
               path('orders/',views.orders,name='orders'),
               path('contact/',views.contact,name='contact')
               
               ]

 
