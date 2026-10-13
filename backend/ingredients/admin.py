from django.contrib import admin
from .models import Ingredient, Grain, Hop

# Register your models here.

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Grain)
class GrainAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'grain_type', 'color_ebc')
    search_fields = ('ingredient__name',)

@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'alpha_acid', 'beta_acid')
    search_fields = ('ingredient__name',)