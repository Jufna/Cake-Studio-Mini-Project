from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import uuid




# Create your models here.
class Cake_studio(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=False,null=False)
    image_url=models.CharField(max_length=2083)
    quantity=models.CharField(max_length=100)



    def __str__(self):
        return self.name
    



# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()

#     def __str__(self):
#         return self.name
    
# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)


#     @property
#     def total(self):
#         return self.quantity * self.product.price  










class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    Image_url=models.ImageField(upload_to='products/')


    def __str__(self):
        return self.name
    


class Cart(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)
    

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartitem')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
    quantity=models.IntegerField(default=0)


    def __str__(self):
        return self.product.name
    