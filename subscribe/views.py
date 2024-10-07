
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from profiles.models import UserProfile
from .models import SubscriptionOrder

@login_required
def subscribe(request):
    user_profile = request.user.UserProfile

    # if user is ot subscribed create an order for the user
    if not user_profile.subscription_active:
        # duration and price of subscription, this will be 1 month (30 days)
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=30) 
        amount = 10.00 
    
    # create the subscription order 
    subscription_order = SubscriptionOrder.objects.create(
        user=request.user,
        start_date=start_date,
        end_date=end_date,
        amount=amount,
        status='active'
    )

    # show updates on users profile
    user_profile.subscription_status = True
    user_profile.current_subscription = subscription_order
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
