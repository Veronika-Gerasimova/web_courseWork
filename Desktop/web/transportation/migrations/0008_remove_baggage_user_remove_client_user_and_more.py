# Generated by Django 5.1.1 on 2024-10-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0007_baggage_user_client_user_flight_user_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baggage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
