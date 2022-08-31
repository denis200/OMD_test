from django.db.models.signals import post_save
from django.dispatch import receiver

from cbu.models import UserTable

from config.settings import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserTable.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, created, **kwargs):
    instance.usertable.save()