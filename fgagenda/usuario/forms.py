from django import forms

class LoginForm(forms.Form):   
    email = forms.EmailField(required=True, label = 'E-mail')
    password = forms.CharField(required=True, label = 'Senha', widget = forms.PasswordInput)