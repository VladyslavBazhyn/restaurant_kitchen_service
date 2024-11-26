"""Models of restaurant kitchen service api."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    """Model of dish types."""

    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Ingredient(models.Model):
    """Model of ingredient, which is a part of dish."""

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    bought_date = models.DateField(
        auto_now_add=True,
    )
    best_before = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.name} for {self.price} bought {self.bought_date}"


class Cook(AbstractUser):
    """Main worker on a kitchen and user on server."""

    years_of_experience = models.IntegerField(null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    """Model of a dish, which consist of different ingredients."""

    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes", null=True)
    cooks = models.ManyToManyField(Cook, related_name="dishes", null=True)

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        """Return the corresponding row."""

        return f"Dish: {self.name} with price: {self.price}"
