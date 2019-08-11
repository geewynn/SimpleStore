from django.contrib import admin
from django.urls import path, include
#from store import urls as app_urls
from store import views

urlpatterns = [
#    path('', include(app_urls)),
    path('', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/', views.removefromcart, name='remove'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/checkout/complete', views.completeOrder, name='complete_order'),
    path('admin-login/', views.adminLogin, name='admin_login'),
    path('admin-panel/', views.adminDashboard, name='admin'),


]