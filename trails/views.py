from django.shortcuts import render
from .models import Trail

def trails(request):
    """A view to return index page """
    return render(request, 'trails/trails.html')


