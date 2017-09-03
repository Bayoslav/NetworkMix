from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate

class Home(View):
    def get(self, request):
        form = UserForm(request.POST)
        return render(request, 'index.html', {'form' : form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #print(request.POST.data)
            return HttpResponse("You're registered.")
        else:
            form = UserForm()
        return render(request, 'index.html', {'form': form})

class LogIn(View):
    def get(self,request):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse("You're logged in Now")
        else:
            return HttpResponse("You failed")
