from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time

# Create your views here.


def index(request):
    return render(request,'website_app/index.html')

def success_view(request):
    return render(request,'website_app/scces.html')

def products_view(request):
    return render(request,'website_app/products.html')
        

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not  None:
            login(request, user)
            return redirect('website_app:success')  # Redirect to a success page
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    
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