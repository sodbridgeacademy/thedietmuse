# Generated by Django 4.0.4 on 2022-04-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='events/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]
