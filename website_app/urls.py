from django.urls import path
from . import views

app_name = 'website_app'

urlpatterns = [
    path('home/', views.index,name ='index'),
    path('login/',views.login_view, name = 'login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',views.LogoutView, name='logout'),
    path('success/', views.success_view, name='success'),
    path('products/', views.products_view, name='products'),
]