from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Ingredient,
    Dish,
    DishType,
    Cook
)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {"fields": ("years_of_experience", )}
            ),
        )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name", "bought_date", "best_before")


admin.site.register(Dish)

admin.site.register(DishType)
