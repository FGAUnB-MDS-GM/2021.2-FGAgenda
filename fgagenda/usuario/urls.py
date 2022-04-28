from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar/', SignupManagerView.as_view(), name='cadastrar'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
