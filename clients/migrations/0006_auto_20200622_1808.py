# Generated by Django 3.0.6 on 2020-06-22 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20200622_1539'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CampaignBudget',
            new_name='Budget',
        ),
    ]