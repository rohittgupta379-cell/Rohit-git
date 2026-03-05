from django.contrib import admin
from django.urls import path
from . import views   # ✅ correct import

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Tracker"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("produch/", views.produch, name="ProductView"),
]