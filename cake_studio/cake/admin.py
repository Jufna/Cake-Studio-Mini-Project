from . models import Cake_studio,Product, CartItem
from django.contrib import admin
from django.contrib.auth.models import Permission



# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    list_display=('name','price','image','quantity')



    
admin.site.register(Cake_studio)
admin.site.register(Permission)
admin.site.register(Product)
admin.site.register(CartItem)










