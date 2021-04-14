from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("collections/<str:query>/", views.collections, name="collection"),
    path("collections/", views.collections, name="collections"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("product/<int:id>/", views.product, name="product"),
    path("add/<int:id>/", views.add, name="add"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout")
]
