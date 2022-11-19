from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conpass = request.POST['conpass']
        myuser = User.objects.create_user(username, email, password)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.conpass = conpass
        myuser.save()
        messages.success(request, 'Your Account Has Been successfully create')
        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pswd = request.POST['pswd']
        user = authenticate(username=username, pawsword=pswd)
        if user is not None:
            login(request, user)
            return render(request, 'singin.html')
        else:
            messages.error(request, 'bad credentials')
        return redirect('home')

    return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')
