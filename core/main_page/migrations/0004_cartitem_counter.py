# Generated by Django 4.2 on 2024-09-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_cartitem_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='counter',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
