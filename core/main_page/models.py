from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    "Модель для хранения продуктов"

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='data/')
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
    

class CartItem(models.Model):
    "Предметы в корзине"
    
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product, blank=True)
    counter = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self) -> str:
        return "Продукты из " + str(self.user)