from django.shortcuts import redirect, render
from .models import FoodItem
from django.db.models import Sum
import requests
import json


def getdata(query):
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    api_request = requests.get(
    api_url, headers={'X-Api-Key': 'wp80FpjEleF0CHYlW1BEIw==ogoqwPdAM0HQ350E'})
    try:
        api = json.loads(api_request.content)
        return api

    except Exception as e:
        api = "oops!  "
        print(e)
        if api == "oops!  ":
            return redirect('/')
        return api
    
def getcalories(api):
    cal = api[0]["calories"]
    return cal

def food_list(request):
    foods = FoodItem.objects.all()
    tcal=0
    for food in foods:
        tcal += food.calories * food.quantity
    print(tcal)
    return render(request, 'food_list.html', {'foods': foods, 'total_calories': tcal})  

def reset_data(request):
    FoodItem.objects.all().delete()
    return redirect('food_list')

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        api=getdata(name)
        cal = getcalories(api)
        
        quantity = request.POST['quantity']
        FoodItem.objects.create(name=name, calories=cal, quantity=quantity)
    return redirect('food_list')

