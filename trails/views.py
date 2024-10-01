from django.shortcuts import render

def trails(request):
    """A view to return index page """
    return render(request, 'trails/trails.html')
