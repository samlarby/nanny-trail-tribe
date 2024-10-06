
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from profiles.models import UserProfile

@login_required
def subscribe(request):
    user_profile = request.user.profile
    user_profile.subscription_active = True
    user_profile.save()
    return redirect('subscription_status')

@login_required
def unsubscribe(request):
    user_profile = request.user.profile
    user_profile.subscription_active = False
    user_profile.save()
    return redirect('subscription_status')


@login_required
def subscription_status(request):
    return render(request, 'subscribe/subscription_status.html')
