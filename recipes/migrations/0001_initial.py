# Generated by Django 4.2.3 on 2024-06-11 19:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0008_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ManyToManyField(to='inventory.ingredient')),
                ('person', models.ManyToManyField(blank=True, default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
