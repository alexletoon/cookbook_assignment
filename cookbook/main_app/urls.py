from django.urls import path

from main_app.views.base import IndexView
from main_app.views.recipe import add_product_to_recipe, cook_recipe, show_recipes_without_product



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_product_to_recipe/', add_product_to_recipe, name='add_product_to_recipe'),
    path('cook_recipe/<int:recipe_id>/', cook_recipe, name='cook_recipe'),
    path('show_recipes_without_product/', show_recipes_without_product, name='show_recipes_without_product'),

]

