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
    


class CartItem(models.Model):
    cart_product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart_quantity} x {self.cart_product_name.product_name}"