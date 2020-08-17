# Generated by Django 3.0.3 on 2020-08-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='catagory',
            field=models.CharField(choices=[('FA', 'Fashion'), ('MW', 'Mam Watches'), ('WW', 'Woman Watches'), ('FJ', 'Fine Jewelry'), ('EW', 'Engagement Wedding'), ('MJ', 'Man Jewelry'), ('VA', 'Vintage Antique'), ('LD', 'Loose Dimonds'), ('LD', 'Loose Beads')], default='FA', max_length=2),
            preserve_default=False,
        ),
    ]