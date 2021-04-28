from django.core.validators import MinLengthValidator
from django.db import models

class Plan(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name="ID",
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=20,
        validators=[MinLengthValidator(1)]
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=50,
        validators=[MinLengthValidator(1)]
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=6, 
        decimal_places=4,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Created At",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Updated At"
    )

    def __str__(self):
        return self.name