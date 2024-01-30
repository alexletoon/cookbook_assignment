from main_app.models import Recipe, Product, RecipeProduct
from django.http import JsonResponse
from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import Http404



@csrf_exempt
def add_product_to_recipe(request):
    recipe_id = request.POST.get('recipe_id')
    product_id = request.POST.get('product_id')
    weight = request.POST.get('weight')

    try:
        recipe_product, created = RecipeProduct.objects.get_or_create(
            recipe_id=recipe_id, 
            product_id=product_id, 
            defaults={'weight_grams': weight})

        if not created:
            recipe_product.weight_grams = weight
            recipe_product.save()

        return JsonResponse({'success': 'Product added/updated in recipe'})
    except IntegrityError:
        return JsonResponse({'error': 'IntegrityError occurred, product_id or recipe_id are not registered'}, status=500)
    

@csrf_exempt
def cook_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    recipe_products = RecipeProduct.objects.filter(recipe=recipe)
    print(recipe_products)
    for recipe in recipe_products:
        recipe.product.number_used_in_dish += 1
        recipe.product.save()
        print(f'{recipe.product.name} - {recipe.product.number_used_in_dish}')

    return JsonResponse({'success': 'Recipe cooked successfully'})


def show_recipes_without_product(request):
    try:
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        recipes_to_exclude = RecipeProduct.objects.filter(product_id=product_id)
        recipe_ids_to_exclude = recipes_to_exclude.values_list('recipe_id', flat=True).distinct()
        recipes_without_product = Recipe.objects.exclude(id__in=recipe_ids_to_exclude)
        recipes_less_10gr = RecipeProduct.objects.filter(weight_grams__lte=10)&RecipeProduct.objects.filter(product_id=product_id)

        context = {
            'product_to_exclude': product,
            'recipes_without_product': recipes_without_product,
            'recipes_less_10gr': recipes_less_10gr,
            'product_id': product_id
            # 'product_not_found': False
        }

        return render(request, 'recipe_table.html', context)
    except Http404:
            context = {
                'product_id': product_id,
                'product_not_found': True,
            }
            return render(request, 'recipe_table.html', context)
