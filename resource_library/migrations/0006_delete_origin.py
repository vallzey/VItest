# Generated by Django 2.0.4 on 2018-04-25 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource_library', '0005_remove_post_origin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Origin',
        ),
    ]