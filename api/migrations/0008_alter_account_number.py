# Generated by Django 5.0.3 on 2024-04-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_account_account_type_alter_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
