# Django imports
from re import template
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# Local imports
from .forms import *
from .models import *
from .decorators import *

# Create your views here.
class SignupManagerView(View):
    template_name = 'login.html'
    
    #@method_decorator(is_manager_or_superuser)
    def get(self, request):
        data = { 'form': SignupManagerForm() }     
        return render(request, 'cadastrar.html', data)
    
    #@method_decorator(is_manager_or_superuser)
    def post(self, request):
        form = SignupManagerForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if password1 == password2:
                Manager.objects.create_user(email=email, password=password1, name=name)
                return HttpResponseRedirect(reverse('login'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }  

        return render(request, 'cadastrar.html', data)


class LoginView(View):
    def get(self, request):
        data = { 'form': LoginForm() }
        return render(request, 'login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)

            # a variavel 'next' contem a url da proxima pagina
            # entao se ela existir, redirecionamos para essa url apos logar
            # caso contrario, vamos para a pagina inicial
            if user is not None and 'next' in request.POST: 
                login(request, user)
                return HttpResponseRedirect(request.POST.get('next'))
            elif user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('inicio'))
        
        data = { 
            'form': form,
            'error': 'E-mail ou senha inválidos'
        }     
        return render(request, 'login.html', data)
    

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))