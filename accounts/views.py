
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'ppp.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname)
                user.save();
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching....')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'ppp.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render (request,'about.html')

def bmi(request):
    return render(request, 'bmi.html')





