"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_page.views import MainPage
from login.views import LoginView
from cart.views import CartView, addProductToCart, delProductOfCart
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from registr.views import RegUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_page'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/reg/', RegUser.as_view(), name = 'reg'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:product_id>/', addProductToCart, name='add_product'),
    path('cart/del/<int:product_id>/', delProductOfCart, name='del_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
