# Generated by Django 4.2.3 on 2023-08-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_alter_cake_studio_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake_studio',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]
