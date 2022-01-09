from django.db import models
from django.contrib.auth.models import Permission, User
from django.db.models.deletion import PROTECT






class ProfileAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=PROTECT)
    
    def __str__(self):
        return self.user.username

    class Meta:
        permissions = [
            ('is_admin', 'Is Admin'),
            
        ]



class ProfileSeller(models.Model):
    user = models.OneToOneField(User, on_delete=PROTECT)
 
    def __str__(self):
      return self.user.username

    class Meta:
        
        permissions = [
            ('is_seller', 'Is Seller'),
            
        ]



class Product(models.Model):
    sku = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50, null=False, unique=True)
    quantity = models.IntegerField()
    price = models.DecimalField( max_digits=9, decimal_places=2)


    def __str__(self):
        return self.name








