from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from plans.models import Plan
from django.db import models

User = get_user_model()


class Subscription(models.Model):
    id = models.AutoField(
        verbose_name="ID",
        primary_key=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    plan = models.ForeignKey(
        "plans.Plan",
        on_delete=models.CASCADE,
        verbose_name="Plan"
    )
    app = models.OneToOneField(
        "apps.App",
        on_delete=models.CASCADE,
        related_name="app",
        verbose_name="App"
    )
    active = models.BooleanField(
        verbose_name="Active"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Created At",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Updated At"
    )