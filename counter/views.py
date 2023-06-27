import json
import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# wp80FpjEleF0CHYlW1BEIw==ogoqwPdAM0HQ350E
# Create your views here.
def getdata(query):
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    api_request = requests.get(
    api_url, headers={'X-Api-Key': 'wp80FpjEleF0CHYlW1BEIw==ogoqwPdAM0HQ350E'})
    try:
        api = json.loads(api_request.content)
        # print(api_request.content)
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

def home(request):

    if request.method == 'POST':
        query = request.POST['query']

        api=getdata(query)
        cal = getcalories(api)
        print(cal)

        if api:
            n=len(api)
            return render(request, 'home.html', {'api': api,'n': n})

        else:
            messages.info(request, 'Please check the spelling or try again with different food item')
            return redirect('home')

    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})