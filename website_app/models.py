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