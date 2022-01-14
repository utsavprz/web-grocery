# Generated by Django 3.2.4 on 2022-01-14 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='defaultUserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_city', models.CharField(max_length=150)),
                ('default_address', models.CharField(max_length=150)),
                ('default_street', models.CharField(max_length=150)),
                ('default_postalcode', models.CharField(max_length=10)),
                ('default_description', models.CharField(max_length=200)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
