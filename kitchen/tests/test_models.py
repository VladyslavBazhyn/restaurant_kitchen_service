import datetime

from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, DishType, Dish, Ingredient


class ModelsTest(TestCase):
    def setUp(self) -> None:

        self.test_date = datetime.date(2000, 1, 1)

        self.cook_1 = Cook.objects.create_user(
            username="Cook_1",
            first_name="First_1",
            last_name="Last_1",
            years_of_experience=1
        )

        self.cook_2 = Cook.objects.create_user(
            username="Cook_2",
            first_name="First_2",
            last_name="Last_2",
            years_of_experience=2
        )

        self.dish_type_1 = DishType.objects.create(
            name="test_type_1",
            description="test_description_test_description_test_description"
        )

        self.dish_type_2 = DishType.objects.create(
            name="test_type_2",
            description="test_description_test_description_test_description"
        )

        self.ingredient_1 = Ingredient.objects.create(
            name="test_ingredient_1",
            price=1,
            description="test_description_test_description_test_description",
        )

        self.ingredient_2 = Ingredient.objects.create(
            name="test_ingredient_2",
            price=2,
            description="test_description_test_description_test_description",
        )

        self.dish_1 = Dish.objects.create(
            name="test_dish_1",
            description="test_description_test_description_test_description",
            price=1.11,
            dish_type=self.dish_type_1,
        )
        self.dish_1.cooks.add(self.cook_1)
        self.dish_1.ingredients.add(self.ingredient_1)

        self.dish_2 = Dish.objects.create(
            name="test_dish_2",
            description="test_description_test_description_test_description",
            price=2.22,
            dish_type=self.dish_type_2,
        )
        self.dish_2.cooks.add(self.cook_1)
        self.dish_2.cooks.add(self.cook_2)
        self.dish_2.ingredients.add(self.ingredient_1)
        self.dish_2.ingredients.add(self.ingredient_2)

    def test_ingredient_fields_correct(self):
        self.assertEqual(
            self.ingredient_1.name,
            "test_ingredient_1"
        )
        self.assertEqual(
            self.ingredient_1.price,
            1
        )
        self.assertEqual(
            self.ingredient_1.description,
            "test_description_test_description_test_description"
        )
        self.assertEqual(
            self.ingredient_1.bought_date,
            datetime.date.today()
        )

    def test_dish_type_fields_correct(self):
        self.assertEqual(
            self.dish_type_1.name,
            "test_type_1"
        )
        self.assertEqual(
            self.dish_type_1.description,
            "test_description_test_description_test_description"
        )

    def test_cook_fields_correct(self):
        self.assertEqual(
            self.cook_1.username,
            "Cook_1"
        )
        self.assertEqual(
            self.cook_1.first_name,
            "First_1"
        )
        self.assertEqual(
            self.cook_1.last_name,
            "Last_1"
        )
        self.assertEqual(
            self.cook_1.years_of_experience,
            1
        )

    def test_dish_fields_correct(self):
        self.assertEqual(
            self.dish_1.name,
            "test_dish_1"
        )
        self.assertEqual(
            self.dish_1.description,
            "test_description_test_description_test_description"
        )
        self.assertEqual(
            self.dish_1.price,
            1.11
        )
        self.assertEqual(
            self.dish_1.dish_type,
            self.dish_type_1
        )
        self.assertEqual(
            list(self.dish_1.ingredients.all()),
            list(Ingredient.objects.filter(name__icontains="test_ingredient_1"))
        )
        self.assertEqual(
            list(self.dish_2.ingredients.all()),
            list(Ingredient.objects.filter(name__icontains="test_ingredient"))
        )
        self.assertEqual(
            list(self.dish_2.cooks.all()),
            list(Cook.objects.filter(username__icontains="Cook"))
        )

    def test_ingredient_str_correct(self):
        self.assertEqual(
            str(self.ingredient_1),
            f"{self.ingredient_1.name}"
            f" for {self.ingredient_1.price} "
            f"bought {self.ingredient_1.bought_date}"
        )

    def test_dish_str_correct(self):
        self.assertEqual(
            str(self.dish_1),
            f"Dish: {self.dish_1.name} with price: {self.dish_1.price}"
        )

    def test_dish_type_str_correct(self):
        self.assertEqual(
            str(self.dish_type_1),
            f"{self.dish_type_1.name}"
        )

    def test_cook_str_correct(self):
        self.assertEqual(
            str(self.cook_1),
            f"{self.cook_1.username} "
            f"({self.cook_1.first_name} "
            f"{self.cook_1.last_name})"
        )

    def test_cook_get_absolute_url_correct(self):
        self.assertEqual(
            self.cook_1.get_absolute_url(),
            reverse("kitchen:cook-detail", kwargs={"pk": self.cook_1.pk})
        )
