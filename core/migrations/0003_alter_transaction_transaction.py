# Generated by Django 5.0.4 on 2024-04-15 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_transactions', to='core.transaction'),
        ),
    ]