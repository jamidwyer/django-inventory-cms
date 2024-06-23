# Generated by Django 4.2.3 on 2024-06-12 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_id', models.TextField(null=True)),
                ('remote', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('following', models.ManyToManyField(related_name='followers', to='inventory.person')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_id', models.TextField(null=True)),
                ('remote', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=500)),
                ('likes', models.ManyToManyField(related_name='liked', to='inventory.person')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='inventory.person')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('person', models.ManyToManyField(to='inventory.person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('unit', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='inventory.quantitativeunit')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_id', models.TextField()),
                ('payload', models.BinaryField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('remote', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='inventory.person')),
            ],
        ),
    ]
