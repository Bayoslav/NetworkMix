from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserForm, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate

class Home(View):
    def get(self, request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        form = UserForm(request.POST)
        return render(request, 'index.html', {'form' : form})

    def post(self, request):
        form = UserForm(request.POST)
        error = 0
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #print(request.POST.data)
            return redirect('/')
        else:
            error = 1
            #form = UserForm()

        return render(request, 'index.html', {'form': form, 'error': error})

class LogIn(View):
    def get(self,request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'dashboard.html')
            except:
                pass

        return render(request, 'login.html', {'form': form, 'error': "Invalid Username & Password!"})

class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        else:
            return redirect('/login/')

    #deal with ajax request submission for facebook/twitter
    def post(self, request):
        data = {'result': 'Okay'}
        return JsonResponse(data)