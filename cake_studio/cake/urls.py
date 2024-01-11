
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('logi',views.loginn,name="logi"),
    path('home',views.home,name="home"),
    path('cake_booking', views.cake_booking, name='cake_booking'),
    path('booking_success', views.booking_success, name='booking_success'),
    path('profile', views.profile, name='profile'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('logout',views.logout_view,name='logout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart')
   

]
