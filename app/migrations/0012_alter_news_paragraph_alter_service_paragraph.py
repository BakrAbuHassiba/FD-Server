# Generated by Django 5.1.1 on 2024-10-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_service_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='paragraph',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='service',
            name='paragraph',
            field=models.TextField(max_length=2500, null=True),
        ),
    ]
