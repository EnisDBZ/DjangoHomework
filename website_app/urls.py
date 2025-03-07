from django.urls import path
from . import views
app_name = 'website_app'

urlpatterns = [
    path('', views.index,name ='index'),
    path('',views.redirect_url_,name="redirect_url"),
    path('login/',views.login_view, name = 'login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',views.LogoutView, name='logout'),
    path('settings/',views.settings_user,name='settings'),
    path('settings/addresses/', views.addresses_settings, name='addresses_settings'),
    path('settings/payment-methods/', views.payment_methods_settings, name='payment_methods_settings'),
    path('payment/',views.payment_methods_settings,name = "payment"),
   
    path('success/', views.success_view, name='success'),
    path('products/', views.products_view, name='products'),
    path('cart/',views.cart_view,name="cart"),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('add/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
    path('remove/<int:item_id>/', views.remove_from_cart, name = "remove_from_cart"),
    
]