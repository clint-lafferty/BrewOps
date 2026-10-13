from django.db import models

# Create your models here.


#Base ingredient model for all ingredients
class Ingredient(models.Model):
    class Category(models.TextChoices):
        GRAIN = "grain", "Grain"
        HOP = "hop", "Hop"
        YEAST = "yeast", "Yeast"
        ADDITIVE = "additive", "Additive"

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


#Grain specific model
class Grain(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='grain_spec')
    grain_type = models.CharField(max_length=100, blank=True, null=True)
    color_ebc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    potential_extract = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.ingredient.name} (Grain)"


#Hop specific model
class Hop(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='hop_spec')
    # Additional fields specific to hops can be added here
    alpha_acid = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    beta_acid = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cohumulone = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    aroma_profile = models.TextField(blank=True, null=True)
    flavor_profile = models.TextField(blank=True, null=True)
    substitution_hops = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.ingredient.name} (Hop)"
