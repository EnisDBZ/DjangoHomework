from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
from .models import Product,CustomUser,CartItem
from .forms import CartItemForm
from decimal import Decimal
from django.http import HttpResponse
from django.utils import translation
from django.conf import settings

# Create your views here.

def redirect_url_(request):
    if request.user.is_authenticated:
        redirect_url = 'index'  # Yönlendirilecek URL
    else:
        redirect_url = 'login'

    return render(request, 'template_name.html', {'redirect_url': redirect_url})


def index(request):
    return render(request,'website_app/index.html')

def success_view(request):
    pass


# !--- Shopping Cart functions

def update_cart_item(request, item_id):
    if request.method == 'POST':
        # Get the CartItem object by its ID
        cart_item = CartItem.objects.get(id=item_id)

        # Get the new quantity from the form
        new_quantity = int(request.POST.get('quantity', cart_item.cart_quantity))  # Default to current quantity if not provided

        # Update the cart item's quantity and save
        cart_item.cart_quantity = new_quantity
        cart_item.save()

    # After updating, redirect the user back to the cart page
    return redirect('website_app:cart')

def products_view(request):
    products = Product.objects.all()
    return render(request,'website_app/products.html',{'products':products})

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.cart_product_name.product_price * item.cart_quantity for item in cart_items)
    return render(request,'website_app/cart.html',{'cart_items':cart_items,'total_price':total_price})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        cart_item, created = CartItem.objects.get_or_create(cart_product_name = product,user = request.user)
        quantity = int(request.POST.get('quantity',1))
        cart_item.cart_quantity += quantity
        cart_item.save()
        return redirect('website_app:products')

    # If it's not a POST request, render the product page with the form
    return render(request, 'website_app/product_detail.html', {'product': product})

def remove_from_cart(request,item_id):
    # Get the cart item based on the item_id
    cart_item = CartItem.objects.get(id=item_id)

    cart_item.delete()

        

    # Redirect to the cart page after updating
    return redirect('website_app:cart')
'''  
    cart_item = CartItem.objects.get(id = item_id)
    cart_item.delete()
    return redirect('website_app:cart')
'''
# Shopping Cart codes ends here !---
User =get_user_model()
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)



        if user is not  None:
            login(request,user)
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('/admin/')  # Redirect to a success page
        
            return render(request,'website_app/index.html')
        else:
            return render(request,'registration/login.html',{'error':'Invalid credentials'})
    # Render the login page for GET requests
    return render(request, 'registration/login.html')

def LogoutView(request):
    logout(request)
    return redirect('website_app:index')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Şifrelerin eşleşip eşleşmediğini kontrol et
        if password != confirm_password:
            messages.error(request, "Şifreler eşleşmiyor.")
            return render(request, 'registration/signup.html')

        # Kullanıcıyı oluştur
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Kayıt başarılı! Giriş yapabilirsiniz.")
            return redirect('website_app:login')  # Giriş sayfasına yönlendir
        except Exception as e:
            messages.error(request, "Kayıt sırasında bir hata oluştu: " + str(e))
            return render(request, 'registration/signup.html')

    return render(request, 'registration/signup.html')