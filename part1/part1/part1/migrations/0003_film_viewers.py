# Generated by Django 2.2.1 on 2019-05-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0002_delete_keeptrack'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='viewers',
            field=models.ManyToManyField(to='part1.Viewer'),
        ),
    ]
