# Generated by Django 3.1.7 on 2022-09-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220909_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='date_needed',
            field=models.DateField(help_text='Day you need this order'),
        ),
    ]
