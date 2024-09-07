from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    "Модель для хранения продуктов"

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='data/')

    def __str__(self) -> str:
        return self.title
    

class Cart(models.Model):
    "Корзина привязанная к определенному пользователю"

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Корзина: " + str(self.user)
    

class CartItem(models.Model):
    "Предметы в корзине"

    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)

    def __str__(self) -> str:
        return str(self.cart)