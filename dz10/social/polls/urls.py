from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logon/', views.logon, name='logon'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
]
