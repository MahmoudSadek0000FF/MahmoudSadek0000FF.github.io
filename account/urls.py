from django.urls import path,include
from . import views

urlpatterns = [

    path('signup',views.register_request, name="register_request"),
    path('login',views.login_request, name="login"),
    
]