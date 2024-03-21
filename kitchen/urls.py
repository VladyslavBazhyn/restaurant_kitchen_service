from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishDetailView,
    DishTypeListView,
    DishTypeDetailView
)

urlpatterns = [
    path("", index),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list:"
    ),
    path(
        "dishes/<int:pk>",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish_types-list:"
    ),
    path(
        "dish_types/<int:pk>",
        DishTypeDetailView.as_view(),
        name="dish_types-detail"
    )
]

app_name = "kitchen"
