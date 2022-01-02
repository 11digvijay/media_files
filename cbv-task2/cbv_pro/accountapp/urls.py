from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.loginview,name='login'),
    path('register/',views.registerview,name='register'),
    path('logout/',views.logoutview,name='logout'),
]