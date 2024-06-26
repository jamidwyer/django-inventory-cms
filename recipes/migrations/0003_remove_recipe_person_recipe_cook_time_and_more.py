# Generated by Django 4.2.3 on 2024-06-25 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_alter_recipe_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='person',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='estimated_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='Default Recipe Name Yum', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
