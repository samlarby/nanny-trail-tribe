from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('trails/', views.trails, name='trails')
]
