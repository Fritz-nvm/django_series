from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class LoginView(LoginView):
    template_name = 'login.html'
    
class LogoutView(LogoutView):
    template_name = 'logout.html'

