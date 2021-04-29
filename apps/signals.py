from plans.models import Plan
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import App
from subscriptions.models import Subscription


@receiver(post_save, sender=App)
def create_app_subscription(sender, instance, created, **kwargs):
    if created:
        new_subscription = Subscription.objects.create(
            user=instance.user,
            plan = Plan.objects.filter(name="Free").first(),
            app = instance,
            active = True
        )
        new_subscription.save()
        instance.subscription = new_subscription
        instance.save()
