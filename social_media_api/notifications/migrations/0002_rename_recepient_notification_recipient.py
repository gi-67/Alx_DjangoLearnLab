# Generated by Django 5.1.1 on 2024-09-22 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='recepient',
            new_name='recipient',
        ),
    ]