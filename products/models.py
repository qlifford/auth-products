from django.db import models
from django.urls import reverse

class Product(models.Model):
    img = models.ImageField(upload_to='product_images')
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100000)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('product-detail', args=str(self.id))
        return reverse('home-page')

