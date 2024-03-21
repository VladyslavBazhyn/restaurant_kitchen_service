from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen.models import Dish, Cook, DishType


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


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all()


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().prefetch_related("dish_type__name")


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all()


class DishTypeListView(generic.ListView):
    model = DishType
    paginated_by = 5


class DishTypeDetailView(generic.DetailView):
    model = DishType
    queryset = DishType.objects.all()
