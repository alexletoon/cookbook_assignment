from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True, verbose_name='Продукт')
    number_used_in_dish = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, verbose_name='Рецепт')
    products = models.ManyToManyField(Product, related_name='recipes', through='main_app.RecipeProduct')

    def __str__(self) -> str:
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_product', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_recipe', on_delete=models.CASCADE)
    weight_grams = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        unique_together = ('recipe', 'product')


    def __str__(self) -> str:
        return f"{self.product.name} - ({self.weight_grams}gr)"