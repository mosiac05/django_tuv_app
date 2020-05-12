# Generated by Django 3.0.5 on 2020-05-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuv_app', '0002_galleryimage_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_file',
        ),
        migrations.AddField(
            model_name='song',
            name='song_link',
            field=models.URLField(default='www', max_length=254),
            preserve_default=False,
        ),
    ]
