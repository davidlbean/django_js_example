from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lookup_city", views.getUserCity, name="lookup_city"),
]
