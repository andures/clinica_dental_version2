# Generated by Django 5.1.5 on 2025-02-01 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_patient_conditions_type_patient_num_expidiente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='tooth_1',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 1'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_10',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 10'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_11',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 11'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_12',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 12'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_13',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 13'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_14',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 14'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_15',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 15'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_16',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 16'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_17',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 17'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_19',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 19'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_2',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 2'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_20',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 20'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_21',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 21'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_22',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 22'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_23',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 23'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_24',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 24'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_25',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 25'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_26',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 26'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_27',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 27'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_28',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 28'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_29',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 29'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_3',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 3'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_30',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 30'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_31',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 31'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_32',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 32'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_4',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 4'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_5',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 5'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_6',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 6'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_7',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 7'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_8',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 8'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tooth_9',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 9'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tooth_18',
            field=models.CharField(blank=True, choices=[('S', 'Sano (S)'), ('A', 'Amalgama (A)'), ('R', 'Resina (R)'), ('C', 'Caries (C)'), ('-', 'Ausente (-)'), ('X', 'Perdido (X)'), ('EI', 'Extracción Indicada (EI)'), ('P', 'Periodontopatias (P)'), ('E', 'Endodoncia (E)'), ('PR', 'Prótesis Removible (PR)'), ('I', 'Incrustación (I)'), ('FR', 'Fractura Dentaria (FR)'), ('S', 'Sellantes (S)'), ('PP', 'Pulpotomía (PP)'), ('PC', 'Pulpectomia (PC)')], max_length=2, null=True, verbose_name='Diente 18'),
        ),
    ]
