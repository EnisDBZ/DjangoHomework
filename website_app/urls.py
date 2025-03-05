from django.urls import path
from . import views

app_name = 'website_app'

urlpatterns = [
    path('', views.index,name ='index'),
    path('',views.redirect_url_,name="redirect_url"),
    path('login/',views.login_view, name = 'login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',views.LogoutView, name='logout'),
    path('success/', views.success_view, name='success'),
    path('products/', views.products_view, name='products'),
    path('cart/',views.cart_view,name="cart"),
    path('add/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
    path('remove/<int:item_id>/', views.remove_from_cart, name = "remove_from_cart"),
    
]