from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=30)


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    time_for_using = models.PositiveIntegerField()
    bought_date = models.DateField(
        auto_now_add=True,
    )
    best_before = models.DateField()

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.best_before = (
                    self.bought_date + timedelta(days=self.time_for_using)
            )
            super().save(*args, **kwargs)


class Cook(AbstractUser):
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
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"Dish: {self.name} with price: {self.price}"
