from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(validators=[EmailValidator()], unique=True)  # E-posta alanı
    password = models.CharField(validators=[MinLengthValidator(8)],max_length=16)
    # Ekstra alanlar eklemek isterseniz buraya ekleyebilirsiniz

    def __str__(self):
        return self.username  # Kullanıcı adını döndür
    

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(null=True)
    product_price = models.DecimalField(max_digits=6,decimal_places=2)
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
    class Meta: 
        verbose_name = "Ürünler"
        verbose_name_plural = "Ürünler"
    


class CartItem(models.Model):
    cart_product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart_quantity} x {self.cart_product_name.product_name}"
    
    def cart_total(self):
        return self.cart_quantity * self.cart_product_name.product_price
class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    address_title = models.CharField(max_length=100,null=True,blank=True)
    full_address = models.CharField(max_length=100, null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.CharField(max_length=20,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.address_title} - {self.user.username}"
    
    class Meta:
        verbose_name = "Kullanıcı Adresleri"
        verbose_name_plural = "Kullanıcı Adresleri"

class CreditCard(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='payment')
    card_number = models.CharField(max_length=16)
    expire_date = models.CharField(max_length=5)# MM/YY
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.user} : **** **** **** {self.card_number[-4:]}"