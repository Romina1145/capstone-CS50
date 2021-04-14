
from django.contrib.auth.models import AbstractUser
from django.db import models
import json
# Create your models here.


class User(AbstractUser):
    pass
    cart = models.ForeignKey(
        "Cart", on_delete=models.CASCADE, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(default="google.com")

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    # image = models.ForeignKey(
    #     "Image", on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.URLField(default="google.com")
    category = models.ForeignKey(
        'Category', related_name='items', on_delete=models.CASCADE, null=True, blank=True)

    def get_display_images(self):
        query = Image.objects.filter(item=self, main_display=True)
        return query or None

    def __str__(self):
        return f'{self.name}'


class Popular(models.Model):
    item = models.ForeignKey(
        'Item', related_name="populars", on_delete=models.CASCADE)
    label = models.CharField(max_length=30)
    value = models.CharField(max_length=20)

    sold_units = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.label} option for {self.item}'

    def get_main_image(self):
        query = Image.objects.filter(option=self, main_display=True)
        if query:
            return query[0]
        else:
            return None


class Image(models.Model):
    item = models.ForeignKey(
        "Item", related_name="images", on_delete=models.CASCADE, null=True)
    option = models.ForeignKey(
        "Popular", related_name="images", on_delete=models.CASCADE, null=True)
    image_url = models.URLField(default="google.com")
    main_display = models.BooleanField(default=False)

    def __str__(self):
        return f'Image of {self.item} with {self.option} op'


class CarouselImage(models.Model):
    image_url = models.URLField(default="google.com")
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    # blank=True, is not required
    item = models.ForeignKey('Item', related_name="carousel_item",
                             on_delete=models.CASCADE, null=True, blank=True)
    main = models.BooleanField(default=True)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class CartItem(models.Model):
    item = models.ForeignKey(
        'Item', on_delete=models.CASCADE, null=True, blank=True)


class Cart(models.Model):
    cart_items = models.ManyToManyField(
        CartItem,  blank=True, related_name="cart_items")
