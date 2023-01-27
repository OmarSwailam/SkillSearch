from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance, email=instance.email, name=instance.name)
        profile.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    user = instance.user
    if created == False:
        user.first_name = instance.name
        user.email = instance.email
        user.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

