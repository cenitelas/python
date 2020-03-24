from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="./polls/static/profile_images/", height_field=None, width_field=None, max_length=200, default='')


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


class Message(models.Model):
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE, default=None)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', default=None)
    message = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)