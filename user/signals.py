from django.db.models.signals import post_save
from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

@receiver(user_logged_in) 
def post_login(sender, user, request, **kwargs):
    user.lat_login = timezone.now()
    user.save()

