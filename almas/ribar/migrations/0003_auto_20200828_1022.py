# Generated by Django 3.0.8 on 2020-08-28 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribar', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='Service_pics'),
        ),
        migrations.AddField(
            model_name='service',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='Service_pics'),
        ),
    ]