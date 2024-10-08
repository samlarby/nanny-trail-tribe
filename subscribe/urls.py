from django.urls import path
from . import views


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('subscription_status/', views.subscription_status, name='subscription_status'),
]