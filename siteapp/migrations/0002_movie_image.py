# Generated by Django 4.1.6 on 2023-04-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='sdgfg', upload_to='movie_images'),
            preserve_default=False,
        ),
    ]
