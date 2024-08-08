# Generated by Django 5.0.4 on 2024-04-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('component_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
