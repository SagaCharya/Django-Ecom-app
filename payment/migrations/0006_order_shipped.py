# Generated by Django 5.1.4 on 2024-12-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_rename_items_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
