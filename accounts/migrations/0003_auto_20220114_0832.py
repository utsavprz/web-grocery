# Generated by Django 3.2.4 on 2022-01-14 02:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_defaultuseraddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='defaultUserAddress',
            new_name='default_User_Address',
        ),
        migrations.RenameModel(
            old_name='UserAddress',
            new_name='User_Address',
        ),
    ]