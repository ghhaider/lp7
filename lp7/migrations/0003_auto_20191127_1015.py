# Generated by Django 2.2.7 on 2019-11-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp7', '0002_about_bgimages_contacteduser_eventbooking_events_eventsheader_galleryisd_galleryrwp_locations_logo_l'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacteduser',
            name='phone',
            field=models.CharField(default='', help_text="Sender's Phone Number", max_length=100, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='phone',
            field=models.CharField(default='', help_text="Sender's Phone Number", max_length=100, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='packagespace',
            name='phone',
            field=models.CharField(default='', help_text="Sender's Phone Number.", max_length=100, verbose_name="Sender's Phone Number"),
        ),
    ]
