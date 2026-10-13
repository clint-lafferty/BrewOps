from django.contrib import admin
from .models import Ingredient, Grain, Hop, Lot, Yeast

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
    list_display = ('ingredient', 'alpha_acid_pct', 'beta_acid_pct', 'cohumulone_pct')
    search_fields = ('ingredient__name',)

@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'lot_number', 'quantity', 'unit_of_measure', 'received_date', 'expiration_date')
    list_filter = ('unit_of_measure',)
    search_fields = ('ingredient__name', 'lot_number')

@admin.register(Yeast)
class YeastAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'strain', 'attenuation', 'flocculation', 'temperature_min_f', 'temperature_max_f')
    search_fields = ('ingredient__name', 'strain')