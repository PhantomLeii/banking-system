# Generated by Django 5.0.3 on 2024-04-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_account_account_type_alter_account_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]