from django.db import models
from shop_app.models import product
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    Date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['Date']
    def __str__(self):
        return '{}'.format(self.cart_id)


class Cartitem(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='Cartitem'
    def subtotal(self):
        return self.products.price*self.quantity
    def __str__(self):
        return '{}'.format(self.products)

