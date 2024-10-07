from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SubscriptionOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) #Links to the user
    created_at = models.DateTimeField(auto_now_add=True) #Get the date of the subscription order
    start_date = models.DateField(default=timezone.now) #The start of the subscription
    end_date = models.DateField() # The end date of the subscription
    amount = models.DecimalField(max_digits=10, decimal_places=2) # price of subscription
    status = models.Charfield(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.status} ({self.start_date} to {self.end_date})"