from django.contrib import admin
from .models import CustomUser,Product,CartItem

# Kullanıcı modelini admin paneline kaydediyoruz
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(CartItem)
