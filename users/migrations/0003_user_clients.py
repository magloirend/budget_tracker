# Generated by Django 3.0.6 on 2020-06-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_organization'),
        ('users', '0002_auto_20200602_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='clients',
            field=models.ManyToManyField(to='clients.Client'),
        ),
    ]
