# Generated by Django 5.0.3 on 2024-04-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kachka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
