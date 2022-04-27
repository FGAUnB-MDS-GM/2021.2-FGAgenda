# Django imports
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Local imports
from .forms import *

# Create your views here.
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
                return HttpResponseRedirect(reverse('home'))
        
        data = { 
            'form': form,
            'error': 'E-mail ou senha inválidos'
        }     
        return render(request, 'login.html', data)