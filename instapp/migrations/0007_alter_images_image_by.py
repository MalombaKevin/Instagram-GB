# Generated by Django 4.0.5 on 2022-06-08 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instapp.profile'),
        ),
    ]