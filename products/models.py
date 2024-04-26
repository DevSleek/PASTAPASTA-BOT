from django.db import models
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    photo = models.ImageField(upload_to='media/photos')
    descreption = models.TextField()
    price = models.CharField(max_length=60)
    weight = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Card(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='card')
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title


class Order(models.Model):
    pass


