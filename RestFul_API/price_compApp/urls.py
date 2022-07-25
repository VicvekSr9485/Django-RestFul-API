from django.urls import path
from . import views


app_name = 'price_compApp'
urlpatterns = [
    path('', views.index, name = 'Pricinghub'),
    path('signup', views.signup, name = 'Signup'),
    path('login', views.LoginView, name = 'Login'),
]