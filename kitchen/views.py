from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen.models import (
    Dish,
    Cook,
    DishType,
    Ingredient
)


def index(request):
    """View function for the home page of the app."""
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_type = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_type": num_dish_type,
        "num_visits": num_visits
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    ordering = ["first_name", "last_name"]


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all()


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all()


class DishTypeListView(generic.ListView):
    model = DishType
    paginated_by = 5
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    context_object_name = "dish_type_detail"
    template_name = "kitchen/dish_type_detail.html"


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 5


class IngredientDetailView(generic.DetailView):
    model = Ingredient


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient


class DishDeleteView(generic.DeleteView):
    model = Dish


class DishUpdateView(generic.UpdateView):
    model = Dish


class DishTypeDeleteView(generic.DeleteView):
    model = DishType


class DishTypeUpdateView(generic.UpdateView):
    model = DishType


class IngredientCreateView(generic.CreateView):
    model = Ingredient


class DishCreateView(generic.CreateView):
    model = Dish


class DishTypeCreateView(generic.CreateView):
    model = DishType


class CookDeleteView(generic.DeleteView):
    model = Cook


class CookUpdateView(generic.UpdateView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
