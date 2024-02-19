# Generated by Django 3.2.23 on 2024-01-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_inventoryitem_expiration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('street_line_1', models.CharField(max_length=255)),
                ('street_line_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
