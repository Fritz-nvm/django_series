from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    
      # authentication urls
    
    path('login/', auth_views.LoginView.as_view(), name='login'), # we use as_view() tp 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   
]