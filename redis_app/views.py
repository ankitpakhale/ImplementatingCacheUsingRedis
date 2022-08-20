from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_recipe(filter_recipe = None):
    if filter_recipe:
        print("Data is coming from DATABASE")
        recipes = Recipe.objects.filter(name__contains = filter_recipe)
    else:      
        recipes = Recipe.objects.all()
    return recipes

def home(request):
    filter_recipe = request.GET.get('recipe')
    if cache.get(filter_recipe):
        print("Data is coming from CACHE")
        recipe = cache.get(filter_recipe)   
    else:   
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe, recipe)
        else: 
            recipe = get_recipe()
    context = {'recipe': recipe}
    return render(request, 'home.html', context)
    
def show(request, id):
    if cache.get(id):
        recipe = Recipe.objects.get(id=id)
        print("SHOW Data CACHE")
    else:
        print("SHOW Data DATABASE")
        recipe = Recipe.objects.get(id=id)
        cache.set(id, recipe)
    context = {'recipe': recipe}
    return render(request, 'show.html', context)