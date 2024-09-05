from django.db import models

# Create your models here.

class Product(models.Model):
    "Модель для хранения продуктов"

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='data/')

    def __str__(self) -> str:
        return self.title