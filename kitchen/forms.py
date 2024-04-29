from django import forms
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

from kitchen.models import (
    Ingredient,
    Dish,
    Cook, DishType
)


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class CookUpdateForm(forms.ModelForm):
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

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    dish_type = forms.ModelChoiceField(
        queryset=DishType.objects.all(),
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class IngredientCreationForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
        widgets = {
            "best_before": DatePickerInput(),
        }


class IngredientUpdateForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = [
            "name", "price", "description"
        ]


class DishUpdateForm(forms.ModelForm):

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "ingredients",
            "cooks"
        ]


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish name"}
        )
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish type name"}
        )
    )
