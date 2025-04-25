from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class LoginView(LoginView):
    template_name = 'login.html'
    
    
class LogoutView(LogoutView):
    template_name = 'logout.html'

class home(request):
    template_name = 'home.html'

class dashboard(request):
    template_name = 'dashboard.html'


