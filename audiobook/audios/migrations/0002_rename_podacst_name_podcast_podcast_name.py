# Generated by Django 3.2 on 2021-04-14 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcast',
            old_name='podacst_name',
            new_name='podcast_name',
        ),
    ]
