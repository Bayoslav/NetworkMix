from django.shortcuts import render
import django.views

# Create your views here.
class Home(View): 
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        #povezemo templejt sa indexom
        #ovde registrujemo
         













