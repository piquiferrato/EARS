# Generated by Django 2.1.2 on 2018-10-18 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20181018_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_technician',
            new_name='isTechnician',
        ),
    ]
