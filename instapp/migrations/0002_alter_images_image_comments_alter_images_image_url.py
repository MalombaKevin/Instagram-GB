# Generated by Django 4.0.5 on 2022-06-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_url',
            field=models.ImageField(upload_to='instagram/'),
        ),
    ]