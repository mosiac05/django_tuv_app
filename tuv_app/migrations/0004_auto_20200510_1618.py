# Generated by Django 3.0.5 on 2020-05-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuv_app', '0003_auto_20200509_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_link',
        ),
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.FileField(default='www', upload_to='uploads/songs'),
            preserve_default=False,
        ),
    ]