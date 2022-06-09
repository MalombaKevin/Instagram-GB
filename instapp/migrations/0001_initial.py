# Generated by Django 4.0.5 on 2022-06-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image_caption', models.CharField(max_length=10000)),
                ('image_url', models.ImageField(blank=True, upload_to='instagram/')),
                ('image_likes', models.IntegerField(default=0)),
                ('image_comments', models.TextField()),
            ],
        ),
    ]