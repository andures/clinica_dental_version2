# Generated by Django 5.1.5 on 2025-02-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_appointment_is_completed_alter_appointment_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='next_appointment',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Próxima Cita'),
        ),
    ]
