from .forms import LoginForm1, LoginForm2, MyRegistrationForm1, MyRegistrationForm2
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login


def login_buyer(request):
        username = "not logged in"

        if request.method == "POST":
            # Get the posted form
            MyLoginForm1 = LoginForm1(request.POST)
            if MyLoginForm1.is_valid():
                username = MyLoginForm1.cleaned_data['buyer_username']
                user= authenticate(username)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Invalid account')

        else:
            MyLoginForm1 = LoginForm1()
        return render(request, 'account/login_buyer.html', {"username": username})


def login_seller(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm2 = LoginForm1(request.POST)
        if MyLoginForm2.is_valid():
            username = MyLoginForm2.cleaned_data['seller_name']
            user = authenticate(username)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')

    else:
        MyLoginForm2 = LoginForm2()
    return render(request, 'account/login_buyer.html', {"username": username})


def register_buyer(request):
    if request.method == 'POST':
        form = MyRegistrationForm1(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            form.save()
            return render(request,'account/login_buyer.html',{'new_user': new_user})
    else:
        form = MyRegistrationForm1()

    return render(request, 'account/register_buyer.html', {'form': form})


def register_seller(request):
    if request.method == 'POST':
        form = MyRegistrationForm2(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            form.save()
            return render(request,'account/login_seller.html',{'new_user': new_user})
    else:
        form = MyRegistrationForm2()

    return render(request, 'account/register_seller.html', {'form': form})



