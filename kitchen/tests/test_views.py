from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Dish, Ingredient, DishType

COOK_LIST_URL = reverse("kitchen:cook-list")
COOK_DETAIL_URL = reverse("kitchen:cook-detail", kwargs={"pk": 1})
COOK_CREATE_URL = reverse("kitchen:cook-create")
COOK_UPDATE_URL = reverse("kitchen:cook-update", kwargs={"pk": 1})
COOK_DELETE_URL = reverse("kitchen:cook-delete", kwargs={"pk": 1})

INGREDIENT_LIST_URL = reverse("kitchen:ingredient-list")
INGREDIENT_DETAIL_URL = reverse("kitchen:ingredient-detail", kwargs={"pk": 1})
INGREDIENT_CREATE_URL = reverse("kitchen:ingredient-create")
INGREDIENT_UPDATE_URL = reverse("kitchen:ingredient-update", kwargs={"pk": 1})
INGREDIENT_DELETE_URL = reverse("kitchen:ingredient-delete", kwargs={"pk": 1})

DISH_LIST_URL = reverse("kitchen:dish-list")
DISH_DETAIL_URL = reverse("kitchen:dish-detail", kwargs={"pk": 1})
DISH_CREATE_URL = reverse("kitchen:dish-create")
DISH_UPDATE_URL = reverse("kitchen:dish-update", kwargs={"pk": 1})
DISH_DELETE_URL = reverse("kitchen:dish-delete", kwargs={"pk": 1})

DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
DISH_TYPE_DETAIL_URL = reverse("kitchen:dish-type-detail", kwargs={"pk": 1})
DISH_TYPE_CREATE_URL = reverse("kitchen:dish-type-create")
DISH_TYPE_UPDATE_URL = reverse("kitchen:dish-type-update", kwargs={"pk": 1})
DISH_TYPE_DELETE_URL = reverse("kitchen:dish-type-delete", kwargs={"pk": 1})


class PublicViewsTest(TestCase):
    def test_login_required_cook_list(self):
        res = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_cook_detail(self):
        res = self.client.get(COOK_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_cook_delete(self):
        res = self.client.get(COOK_DELETE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_cook_update(self):
        res = self.client.get(COOK_UPDATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_cook_create(self):
        res = self.client.get(COOK_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_ingredient_list(self):
        res = self.client.get(INGREDIENT_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_ingredient_detail(self):
        res = self.client.get(INGREDIENT_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_ingredient_delete(self):
        res = self.client.get(INGREDIENT_DELETE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_ingredient_update(self):
        res = self.client.get(INGREDIENT_UPDATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_ingredient_create(self):
        res = self.client.get(INGREDIENT_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_list(self):
        res = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_detail(self):
        res = self.client.get(DISH_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_delete(self):
        res = self.client.get(DISH_DELETE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_update(self):
        res = self.client.get(DISH_UPDATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_create(self):
        res = self.client.get(DISH_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_type_list(self):
        res = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_type_detail(self):
        res = self.client.get(DISH_TYPE_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_type_create(self):
        res = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_type_update(self):
        res = self.client.get(DISH_TYPE_UPDATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish_type_delete(self):
        res = self.client.get(DISH_TYPE_DELETE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateViewsTest(TestCase):
    def setUp(self) -> None:
        self.cook = Cook.objects.create_user(
            username="Test username",
            years_of_experience=1,
            first_name="Test name",
            last_name="Test surname",
            password="Test parol"
        )
        self.client.force_login(self.cook)

        self.cook_2 = Cook.objects.create_user(
            username="Test username 2",
            years_of_experience=2,
            first_name="Test name",
            last_name="Test surname",
            password="Test parol"
        )

        self.dish_type = DishType.objects.create(
            name="test_type_1",
            description="test_description_test_description_test_description"
        )

        self.dish_type_2 = DishType.objects.create(
            name="test_type_2",
            description="test_description_test_description_test_description"
        )

        self.ingredient = Ingredient.objects.create(
            name="test_ingredient_1",
            price=1,
            description="test_description_test_description_test_description",
        )

        self.ingredient_2 = Ingredient.objects.create(
            name="test_ingredient_2",
            price=2,
            description="test_description_test_description_test_description",
        )

        self.ingredient_3 = Ingredient.objects.create(
            name="test_ingredient_3",
            price=3,
            description="test_description_test_description_test_description",
        )

        self.dish = Dish.objects.create(
            name="test_dish_1",
            description="test_description_test_description_test_description",
            price=1.11,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

        self.dish_2 = Dish.objects.create(
            name="test_dish_2",
            description="test_description_test_description_test_description",
            price=2.22,
            dish_type=self.dish_type,
        )

    # Test for ingredient views
    def test_retrieve_ingredient_list_view(self):
        res = self.client.get(INGREDIENT_LIST_URL)
        self.assertEqual(res.status_code, 200)

        ingredient_list = Ingredient.objects.all()
        self.assertEqual(
            list(res.context["ingredient_list"]),
            list(ingredient_list)
        )

    def test_retrieve_ingredient_detail_view(self):
        res = self.client.get(INGREDIENT_DETAIL_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_ingredient_create_view(self):
        res = self.client.get(INGREDIENT_CREATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_ingredient_update_view(self):
        res = self.client.get(INGREDIENT_UPDATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_ingredient_delete_view(self):
        res = self.client.get(INGREDIENT_DELETE_URL)
        self.assertEqual(res.status_code, 200)

    # Tests for dish views
    def test_retrieve_dish_list_view(self):
        res = self.client.get(DISH_LIST_URL)
        self.assertEqual(res.status_code, 200)

        dish_list = Dish.objects.all()
        self.assertEqual(
            list(res.context["dish_list"]),
            list(dish_list)
        )

    def test_retrieve_dish_detail_view(self):
        res = self.client.get(DISH_DETAIL_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_create_view(self):
        res = self.client.get(DISH_CREATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_update_view(self):
        res = self.client.get(DISH_UPDATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_delete_view(self):
        res = self.client.get(DISH_DETAIL_URL)
        self.assertEqual(res.status_code, 200)

    # Tests for dish_type views
    def test_retrieve_dish_type_list_view(self):
        res = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(res.status_code, 200)

        dish_type_list = DishType.objects.all()
        self.assertEqual(
            list(res.context["dish_type_list"]),
            list(dish_type_list)
        )

    def test_retrieve_dish_type_detail_view(self):
        res = self.client.get(DISH_TYPE_DETAIL_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_type_create_view(self):
        res = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_type_update_view(self):
        res = self.client.get(DISH_TYPE_UPDATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_type_delete_view(self):
        res = self.client.get(DISH_TYPE_DELETE_URL)
        self.assertEqual(res.status_code, 200)

    # Tests for cook views
    def test_retrieve_cook_list_view(self):
        res = self.client.get(COOK_LIST_URL)
        self.assertEqual(res.status_code, 200)

        cook_list = Cook.objects.all()
        self.assertEqual(
            list(res.context["cook_list"]),
            list(cook_list)
        )

    def test_retrieve_cook_detail_view(self):
        res = self.client.get(COOK_DETAIL_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_cook_create_view(self):
        res = self.client.get(COOK_CREATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_cook_update_view(self):
        res = self.client.get(COOK_UPDATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_cook_delete_view(self):
        res = self.client.get(COOK_DELETE_URL)
        self.assertEqual(res.status_code, 200)

    # Tests for searching features
    def test_searching_ingredient_list_view(self):
        queryset_filtered = Ingredient.objects.filter(name__icontains="1")
        response = self.client.get(INGREDIENT_LIST_URL, {"name": "test_ingredient_1"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(queryset_filtered)
        )

    def test_searching_dish_list_view(self):
        queryset_filtered = Dish.objects.filter(name__icontains="1")
        response = self.client.get(DISH_LIST_URL, {"name": "test_dish_1"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(queryset_filtered)
        )

    def test_searching_dish_type_list_view(self):
        queryset_filtered = DishType.objects.filter(name__icontains="2")
        response = self.client.get(DISH_TYPE_LIST_URL, {"name": "test_type_2"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(queryset_filtered)
        )

    def test_searching_cook_list_view(self):
        queryset_filtered = Cook.objects.filter(username__icontains="2")
        response = self.client.get(COOK_LIST_URL, {"username": "2"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(queryset_filtered)
        )
