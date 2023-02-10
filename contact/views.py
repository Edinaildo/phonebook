from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def loginView(request):
    authenticationForm = AuthenticationForm()
    if request.method=="POST":
        authenticationForm = AuthenticationForm(request, data=request.POST or None)
        if authenticationForm.is_valid():
            username = authenticationForm.cleaned_data["username"]
            password = authenticationForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("index")
            else:
                print(authenticationForm.errors)

    return render(request, template_name="login.html", context={"authenticationForm": authenticationForm})

def index(request):
    return render(request, template_name="index.html", context={})

def registration(request):
    userCreationForm = UserCreationForm()
    if request.method=="POST":
        userCreationForm = UserCreationForm(request.POST or None)
        if userCreationForm.is_valid():
            username = userCreationForm.cleaned_data["username"]
            password = userCreationForm.cleaned_data["password1"]
            userCreationForm = userCreationForm.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("index")
    else:
        print(userCreationForm.errors)
    return render(request, template_name="registration.html", context={"UserCreationForm" :UserCreationForm})
