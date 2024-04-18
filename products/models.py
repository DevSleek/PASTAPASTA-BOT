from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=60)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='relations', blank=True, null=True)


class Product(models.Model):
    title = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='media/photos')
    descreption = models.TextField()
    price = models.CharField(max_length=60)
    weight = models.CharField(max_length=60)

