# Generated by Django 4.1.7 on 2023-05-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='game_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
