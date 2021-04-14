from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import User, Category, Item, Item, CarouselImage, Popular, Cart, CartItem

# Create your views here.


def home(request):
    carousel = CarouselImage.objects.filter(main=True)
    categories = Category.objects.all()
    mostPopular = Popular.objects.order_by('-sold_units')[:10]
    newestAdditions = Popular.objects.order_by('-id')[:10]
    return render(request, 'RoMoCcino/index.html', {
        'carousel': carousel,
        'categories': categories,
        'popular': mostPopular,
        'newest': newestAdditions
    })


def product(request, id):

    return render(request, "RoMoCcino/product.html", {
        "item": Item.objects.get(pk=id)
    })


def add(request, id):
    cart = request.user.cart

    if cart == None:
        cart = Cart.objects.create()
        request.user.cart_id = cart.id
        cart.save()
        request.user.save()
    cart_item = CartItem.objects.create()
    cart_item.item_id = id
    cart_item.save()
    cart.cart_item_id = cart_item.id
    cart.save()
    return redirect("/cart")


def cart(request):
    cart = request.user.cart
    cart = Cart.objects.get(pk=1)
    cart_items = CartItem.objects.all()
    return render(request, "RoMoCcino/cart.html", {
        "cart_items": cart_items,
    })


def collections(request, query=""):
    carousel = CarouselImage.objects.filter(main=True)
    categories = Category.objects.all().values()
    items_values = Item.objects.all().values()
    # # convert into a list of objects
    items_json = json.dumps(list(items_values), cls=DjangoJSONEncoder)
    items = Item.objects.all()

    return render(request, 'RoMoCcino/collections.html', {
        'carousel': carousel,
        'categories': categories,
        'items': items,
        'items_json': items_json,
        'query': query

    })


def checkout(request):
    CartItem.objects.all().delete()
    cart = request.user.cart
    cart = Cart.objects.get(pk=1)
    cart_items = CartItem.objects.all()
    return render(request, "RoMoCcino/cart.html", {
        "cart_items": cart_items,
        "message": "Thank you for choosing Romy's Coffee!"
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "RoMoCcino/register/html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "RoMoCcino/register.html", {
                "message": "Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse, ("home"))
    else:
        return render(request, "RoMoCcino/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "RoMoCcino/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "RoMoCcino/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
