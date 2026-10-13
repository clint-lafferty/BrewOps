from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ingredient, Grain, Hop, Yeast
from django.core.exceptions import ValidationError


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


class IngredientSpecificationValidationTests(TestCase):
    def test_grain_rejects_hop_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="Cascade",
            category=Ingredient.Category.HOP,
        )
        grain = Grain(ingredient=ingredient)

        with self.assertRaises(ValidationError):
            grain.full_clean()

    def test_hop_rejects_grain_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="Pale Malt",
            category=Ingredient.Category.GRAIN,
        )
        hop = Hop(ingredient=ingredient)

        with self.assertRaises(ValidationError):
            hop.full_clean()

    def test_yeast_rejects_hop_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="Cascade",
            category=Ingredient.Category.HOP,
        )
        yeast = Yeast(ingredient=ingredient)

        with self.assertRaises(ValidationError):
            yeast.full_clean()

    def test_grain_accepts_grain_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="Pale Malt",
            category=Ingredient.Category.GRAIN,
        )
        grain = Grain(ingredient=ingredient)

        grain.full_clean()
