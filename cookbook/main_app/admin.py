from django.contrib import admin

from main_app.models import Product, Recipe, RecipeProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_used_in_dish']
    list_filter = ['name', 'number_used_in_dish']
    search_fields = ['name', 'number_used_in_dish']
    fields = ['name', 'number_used_in_dish']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name']


class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'product', 'weight_grams']
    list_filter = ['recipe', 'product', 'weight_grams']
    search_fields = ['recipe', 'product', 'weight_grams']
    fields = ['recipe', 'product', 'weight_grams']


admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeProduct, RecipeProductAdmin)