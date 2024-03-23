from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    ordering = ["first_name", "last_name"]


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all()


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.all()


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginated_by = 5
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    context_object_name = "dish_type_detail"
    template_name = "kitchen/dish_type_detail.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
