# Generated by Django 3.2.4 on 2022-01-14 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220114_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='default_User_Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user_address'),
        ),
        migrations.DeleteModel(
            name='default_User_Address',
        ),
    ]
