from django.contrib import admin
from .models import CustomUser

# Kullanıcı modelini admin paneline kaydediyoruz
admin.site.register(CustomUser)
