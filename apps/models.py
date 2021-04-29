from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

User = get_user_model()


class App(models.Model):
    app_types = [
        ('Web', 'Web'),
        ('Mobile', 'Mobile')
    ]
    frameworks = [
        ('Django', 'Django'),
        ('React Native', 'React Native')
    ]
    id = models.AutoField(
        verbose_name="ID",
        primary_key=True
    )
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(1)],
        verbose_name="Name")
    description = models.CharField(
        max_length=50, 
        verbose_name="Description",
        null=True)
    type = models.CharField(
        max_length=20,
        choices=app_types,
        verbose_name="Type"
    )
    framework = models.CharField(
        max_length=20,
        choices=frameworks,
        verbose_name="Framework"
    )
    domain_name = models.CharField(
        max_length=50,
        verbose_name="Domain Name",
        null=True
    )
    screenshot = models.CharField(
        max_length=100,
        verbose_name="Screenshot",
        null=True
    )
    subscription = models.OneToOneField(
        "subscriptions.Subscription",
        on_delete=models.CASCADE,
        verbose_name="Subscription",
        related_name="subscription",
        null=True,
    )
    user = models.ForeignKey(
        User,
        related_name="app_user",
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Updated At"
    )

    def __str__(self):
        return self.name