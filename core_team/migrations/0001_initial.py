# Generated by Django 5.0 on 2023-12-13 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='core_team_pictures')),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('current_qualification', models.CharField(max_length=50)),
                ('phone_number', models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999999)])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
