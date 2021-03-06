# Generated by Django 2.2.19 on 2021-04-29 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Name')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=20, verbose_name='Type')),
                ('framework', models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], max_length=20, verbose_name='Framework')),
                ('domain_name', models.CharField(max_length=50, null=True, verbose_name='Domain Name')),
                ('screenshot', models.CharField(max_length=100, null=True, verbose_name='Screenshot')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
