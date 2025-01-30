# Generated by Django 5.1.5 on 2025-01-30 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_patient_age_patient_alcohol_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='conditions_type',
            field=models.CharField(blank=True, choices=[('generalized', 'Generalizada'), ('localized', 'Localizada')], default='generalized', max_length=20, null=True, verbose_name='Tipo de afección'),
        ),
        migrations.AddField(
            model_name='patient',
            name='num_Expidiente',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número De Expediente'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_18',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], default='S', max_length=2, null=True, verbose_name='18'),
        ),
    ]
