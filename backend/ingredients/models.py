from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):
        super().clean()

        if (self.ingredient_id and self.ingredient.category != Ingredient.Category.GRAIN):
            raise ValidationError({
                "ingredient": ("A Grain specification must belong to a grain ingredient.")
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ingredient.name} (Grain)"


#Hop specific model
class Hop(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='hop_spec')
    # Additional fields specific to hops can be added here
    alpha_acid_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    beta_acid_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cohumulone_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    aroma_profile = models.TextField(blank=True, null=True)
    flavor_profile = models.TextField(blank=True, null=True)
    substitution_hops = models.ManyToManyField('self', blank=True)

    def clean(self):
        super().clean()

        if (self.ingredient_id and self.ingredient.category != Ingredient.Category.HOP):
            raise ValidationError({
                "ingredient": ("A Hop specification must belong to a hop ingredient.")
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ingredient.name} (Hop)"

class Yeast(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='yeast_spec')
    # Additional fields specific to yeast can be added here
    strain = models.CharField(max_length=100, blank=True, null=True)
    attenuation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    flocculation = models.CharField(max_length=50, blank=True, null=True)
    temperature_min_f = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperature_max_f = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def clean(self):
        super().clean()

        if (self.ingredient_id and self.ingredient.category != Ingredient.Category.YEAST):
            raise ValidationError({
                "ingredient": ("A Yeast specification must belong to a yeast ingredient.")
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ingredient.name} (Yeast)"

class Lot(models.Model):
    class  UnitOfMeasure(models.TextChoices):
        POUND = "lb", "Pound"
        OUNCE = "oz", "Ounce"
        GALLON = "gal", "Gallon"
        FLUID_OUNCE = "fl_oz", "Fluid Ounce"
        EACH = "ea", "Each"
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='lots')
    lot_number = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_of_measure = models.CharField(max_length=10, choices=UnitOfMeasure.choices)
    received_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Lot {self.lot_number} of {self.ingredient.name}"
