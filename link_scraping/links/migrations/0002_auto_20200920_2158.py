# Generated by Django 3.0.5 on 2020-09-21 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grandchildlink',
            old_name='parent_link',
            new_name='child_link',
        ),
    ]