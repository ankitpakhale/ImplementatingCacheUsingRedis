from django.shortcuts import render
from .models import *
# Create your views here.

def get_recipe(filter_recipe = None):
    recipes = Recipe.objects.all()
    return recipes

def home(request):
    filter_recipe = request.GET.get('recipe')
    recipe = get_recipe()
    context = {'recipe': recipe}
    return render(request, 'home.html', context)
    
def show(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    return render(request, 'show.html', context)
    