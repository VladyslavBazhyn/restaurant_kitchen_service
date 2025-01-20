"""Url patterns for kitchen."""

from django.urls import path

from kitchen.views import (
    index,
    CookAssignDish,
    CookListView,
    CookDetailView,
    CookDeleteView,
    CookUpdateView,
    CookCreateView,
    DishListView,
    DishDetailView,
    DishDeleteView,
    DishUpdateView,
    DishCreateView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishTypeCreateView,
    IngredientListView,
    IngredientDetailView,
    IngredientDeleteView,
    IngredientUpdateView,
    IngredientCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("cook/create", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path(
        "ingredient/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"
    ),
    path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dish_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "ingredient/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredient/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path(
        "ingredient/create/", IngredientCreateView.as_view(), name="ingredient-create"
    ),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path(
        "dish/<int:pk>/toggle-assign/",
        CookAssignDish.as_view(),
        name="toggle-dish-assign",
    ),
]

app_name = "kitchen"
