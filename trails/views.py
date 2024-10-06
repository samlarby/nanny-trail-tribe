from django.shortcuts import render
from .models import Trail


def trails(request):
    """Query the database for Trail objects
       Then pass the objects to the trails template
    """
    trails = Trail.objects.all()

    return render(request, 'trails/trails.html', {'trails': trails})




