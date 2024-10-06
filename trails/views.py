from django.shortcuts import render
from .models import Trail


def trails(request):
    """Query the database for Trail objects
       Then pass the objects to the trails template
    """
    trails = Trail.objects.all()

    # check if user is subscribed through the profile app
    user_is_subscribed = request.user.profile.subscription_active if request.user.is_authenticate else False

    return render(request, 'trails/trails.html', {
      'trails': trails,
      'user_is_subscribed': user_is_subscribed,
    })




