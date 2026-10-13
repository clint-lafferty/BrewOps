from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ingredient


# Create your tests here.


class IngredientAPITestCase(TestCase):
    def test_list_ingredients(self):
        Ingredient.objects.create(name="Cascade", category="hop")

        response = self.client.get("/api/ingredients/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Cascade")

    def test_create_ingredient(self):
        payload = {"name": "Mosaic", "category": "hop"}

        response = self.client.post("/api/ingredients/",
                        payload,
                        format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ingredient.objects.filter(name="Mosaic", category="hop").exists())