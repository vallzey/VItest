# Generated by Django 2.0.4 on 2018-04-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_library', '0006_delete_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
