# Generated by Django 4.2 on 2023-04-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]