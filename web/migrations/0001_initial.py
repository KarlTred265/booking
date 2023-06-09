# Generated by Django 3.2.19 on 2023-05-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('date', models.DateField(verbose_name='Booking Date')),
                ('time', models.CharField(choices=[('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00')], max_length=10, verbose_name='Booking Time')),
                ('booking_ref', models.CharField(max_length=10, verbose_name='Booking Reference')),
                ('num_of_guests', models.IntegerField(verbose_name='Number of Guests')),
                ('message', models.TextField(blank=True, verbose_name='Additional Message')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
