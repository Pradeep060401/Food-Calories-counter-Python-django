from django.shortcuts import render
from .models import FoodItem

def food_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'food_list.html')

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        FoodItem.objects.create(name=name, calories=calories)
    return render(request, 'add_food.html')

