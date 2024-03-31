from django.core.exceptions import ValidationError
from django.test import TestCase

from kitchen.forms import CookCreationForm


class CookCreationFormTest(TestCase):
    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "password123egege",
            "password2": "password123egege",
            "years_of_experience": 1,
            "first_name": "test first name",
            "last_name": "test last name"
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
