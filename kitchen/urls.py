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
    DishTypeDetailView,
    IngredientListView,
    IngredientDetailView
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
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
        name="dishes-list"
    ),
    path(
        "dishes/<int:pk>",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish_types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-types-detail"
    ),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredient-detail"
    ),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list"
    )
]

app_name = "kitchen"
