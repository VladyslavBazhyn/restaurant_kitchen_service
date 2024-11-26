"""Forms of used models."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

from kitchen.models import Ingredient, Dish, Cook, DishType


class CookCreationForm(UserCreationForm):
    """Form for creation a new user."""

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class CookUpdateForm(forms.ModelForm):
    """Form for updating some data in user's profile."""

    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
            "dishes",
        ]


class DishCreationForm(forms.ModelForm):
    """Form for creating a new dish."""

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    dish_type = forms.ModelChoiceField(queryset=DishType.objects.all(), required=False)

    class Meta:
        model = Dish
        fields = "__all__"


class IngredientCreationForm(forms.ModelForm):
    """Form for creation a new ingredient."""

    class Meta:
        model = Ingredient
        fields = "__all__"
        widgets = {
            "best_before": DatePickerInput(),
        }


class IngredientUpdateForm(forms.ModelForm):
    """Form for update some ingredient's data."""

    class Meta:
        model = Ingredient
        fields = ["name", "price", "description"]


class DishUpdateForm(forms.ModelForm):
    """Form for update some dish's data."""

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "ingredients", "cooks"]


class CookSearchForm(forms.Form):
    """Form for searching through all cooks."""

    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class IngredientSearchForm(forms.Form):
    """Form for searching through all ingredients."""

    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class DishSearchForm(forms.Form):
    """Form for searching through all dishes."""

    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by dish name"}),
    )


class DishTypeSearchForm(forms.Form):
    """Form for searching through all dish types."""

    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by dish type name"}),
    )
