from django.contrib import admin

# Register your models here.
from .models import User, Category, Item, Image, CarouselImage, Popular, Cart, CartItem


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(CarouselImage)
admin.site.register(Popular)
admin.site.register(Cart)
admin.site.register(CartItem)
