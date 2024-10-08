
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from profiles.models import UserProfile
from .forms import SubscriptionForm
from .models import SubscriptionOrder

@login_required
def subscribe(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
                
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)

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

                return render(request, 'subscribe/subscribe.html')
    else:
        form = SubscriptionForm()

    # if user already is subscribed redirect them to subscription_status
    return render(request,'subscribe/subscribe.html', {'form': form})



@login_required
def unsubscribe(request):
    user_profile = request.user.UserProfile

    # cancel subscription
    if user_profile.subscription_active and user_profile.current_subscription:
        current_order = user_profile.current_subscription
        current_order.status = 'cancelled'
        current_order.save()

        # deactivate user current subscription in the users profile
        user_profile.subscription_active = False
        user_profile.current_subscription = None
        user_profile.save()

    return redirect('subscription_status')


@login_required
def subscription_status(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    current_order = user_profile.current_subscription

    return render(request, 'subscribe/subscription_status.html', {
        'subscription_active': user_profile.subscription_active,
        'current_order': current_order,
    })
