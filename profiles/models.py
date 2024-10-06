from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user model for maintaining users information

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_active = models.BooleanField(default=False)

    name = models.CharField(max_length=20, null=True, blank=True)
    riding_style = models.CharField(max_length=20, null=True, blank=True)
    favourite_place_to_ride = models.CharField(max_length=50, null=True, blank=True)
    local_trails = models.CharField(max_length=50, null=True, blank=True)
    bike = models.CharField(max_length=50, null=True, blank=True)
    favourite_conditions = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ create or update user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()