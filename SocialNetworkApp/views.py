from django.shortcuts import render
from django.http import HttpResponse

from . import models
from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home_page(request):
    uname = request.POST['username']
    pw = request.POST['password']
    dbuname = User.objects.filter(username=uname).exists()
    dbpw = User.objects.filter(password=pw).exists()
    if (dbuname and dbpw):
        return render(request, 'home.html')
    else:
        return render(request, 'index.html', {'message': 'Invalid Credentials'})


def sign_up(request):
    return render(request, 'signup.html')


def insert(request):
    credential = models.User(username=request.POST['username'],
                             password=request.POST['password'],
                             firstname=request.POST['firstname'],
                             lastname=request.POST['lastname'],
                             repassword=request.POST['rpassword'])
    try:
        credential.save()
        return render(request, 'register.html')
    except Exception as e:
        return HttpResponse(e)


def profile(request):
    user_name = request.POST['username']
    pw = request.POST['password']


    # user_id = RegisteredUser.objects.only('id').get(username=user_name).exists().id
    user_id = User.objects.filter(username=user_name).values_list('id', flat=True).first()
    user_fn = User.objects.filter(username=user_name).values_list('firstname', flat=True).first()
    authusername = User.objects.filter(username=user_name, password=pw).exists()
    # db_password = RegisteredUser.objects.filter(password=pw).exists()

    test = User.objects.filter(username=user_name, password=pw).values()

    print(test[0]['username'])
    print(test[1]['password'])
    print(user_id)
    print(user_fn)



    if (authusername):
        return render(request, 'profile.html',
                      {'user': User.objects.filter(username=user_name, password=pw).values()[0]})
    else:
        return render(request, 'index.html', {'message': 'Invalid Credentials'})
