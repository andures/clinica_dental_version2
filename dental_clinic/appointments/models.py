from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
class Patient(models.Model):
    # Datos Generales
    name = models.CharField(max_length=100, verbose_name="Nombre Del Paciente")
    age = models.IntegerField(default=0, verbose_name="Edad", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo Electrónico", null=True, blank=True)
    birth_date = models.DateField(verbose_name="Fecha De Nacimiento", null=True, blank=True)
    num_Expidiente = models.CharField(max_length=50, verbose_name="Número De Expediente", null=True, blank=True)
    identity_number = models.CharField(max_length=50, verbose_name="Número De Identidad", null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('F', 'Femenino'), ('M', 'Masculino')], verbose_name="Género", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Teléfono", null=True, blank=True)
    next_appointment = models.DateTimeField(null=True, blank=True, verbose_name="Próxima Cita")
    dentist = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Dentista")

    # Campos adicionales
    origin = models.CharField(max_length=100, verbose_name="Lugar De Procedencia", null=True, blank=True)
    neighborhood = models.CharField(max_length=100, verbose_name="Barrio / Colonia / Residencial", null=True, blank=True)
    responsible_name = models.CharField(max_length=100, verbose_name="Nombre Del Responsable", null=True, blank=True)
    relationship = models.CharField(max_length=50, verbose_name="Relación / Parentesco", null=True, blank=True)
    responsible_phone = models.CharField(max_length=15, verbose_name="Teléfono Del Responsable", null=True, blank=True)
    hospitalized_last_2_years = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Ha sido hospitalizado en los últimos dos años?", null=True, blank=True)
    hospitalization_reason = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿Por qué?")
    under_medical_treatment = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Está bajo tratamiento médico por enfermedad?", null=True, blank=True)
    medical_condition = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿Sí, qué enfermedad?")
    allergic_to_substances = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Es alérgico a alguna sustancia, alimento o droga?", null=True, blank=True)
    allergies_detail = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿A qué?")
    regular_medications = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿Qué medicamentos consume habitualmente?")
    smokes = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Fuma?", null=True, blank=True)
    cigarettes_per_day = models.IntegerField(blank=True, null=True, default=0, verbose_name="¿Cuántos al día?")
    drinks_alcohol = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Toma alcohol?", null=True, blank=True)
    alcohol_amount = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name="¿Cuánto?")
    is_pregnant = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Está embarazada?", null=True, blank=True)
    pregnancy_months = models.IntegerField(blank=True, null=True, default=0, verbose_name="¿Cuántos meses?")
    
    CONDITIONS_CHOICES = [
        ('cardiac_problems', 'Problemas Cardiacos'),
        ('high_blood_pressure', 'Presión Sanguínea Alta'),
        ('low_blood_pressure', 'Presión Sanguínea Baja'),
        ('venereal_diseases', 'Enfermedades Venéreas'),
        ('hepatitis', 'Hepatitis'),
        ('stomach_ulcers', 'Úlceras Estomacales'),
        ('headaches', 'Dolor De Cabeza'),
        ('aids', 'Sida'),
        ('epilepsy', 'Epilepsia'),
        ('arthritis', 'Artritis'),
        ('diabetes', 'Diabetes'),
        ('nervous_issues', 'Alteraciones nerviosas'),
        ('sinusitis', 'Sinusitis'),
        ('other', 'Otras')
    ]
    
    conditions = MultiSelectField(choices=CONDITIONS_CHOICES, default='', verbose_name="Afecciones", null=True, blank=True)
    observations = models.TextField(blank=True, null=True, default='', verbose_name="Observaciones")
    attach_medical_report = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="Adjunta el informe médico", null=True, blank=True)
    difficulty_speaking = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Tiene dificultad para hablar?", null=True, blank=True)
    difficulty_chewing = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Para masticar?", null=True, blank=True)
    difficulty_opening_mouth = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Para abrir la boca?", null=True, blank=True)
    difficulty_swallowing = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Para tragar los alimentos?", null=True, blank=True)
    bleeding_gums = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Le sangran las encías?", null=True, blank=True)
    tooth_mobility = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Tiene movilidad en algún diente?", null=True, blank=True)
    pus_in_mouth = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="¿Le sale pus de algún lugar de la boca?", null=True, blank=True)
    pus_location = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿Dónde?")
    brushing_frequency = models.IntegerField(default=0, verbose_name="¿Cuántas veces al día se cepilla los dientes?", null=True, blank=True)
    oral_hygiene_status = models.CharField(max_length=10, choices=[('good', 'Buena'), ('regular', 'Regular'), ('poor', 'Mala')], default='good', verbose_name="¿Estado de la higiene bucal?", null=True, blank=True)
    tongue_condition = models.CharField(max_length=10, choices=[('abnormal', 'Anormal'), ('normal', 'Normal')], default='normal', verbose_name="Lengua", null=True, blank=True)
    lips_condition = models.CharField(max_length=10, choices=[('abnormal', 'Anormal'), ('normal', 'Normal')], default='normal', verbose_name="Labios", null=True, blank=True)
    cheeks_condition = models.CharField(max_length=10, choices=[('abnormal', 'Anormal'), ('normal', 'Normal')], default='normal', verbose_name="Carillos", null=True, blank=True)
    floor_of_mouth_condition = models.CharField(max_length=10, choices=[('abnormal', 'Anormal'), ('normal', 'Normal')], default='normal', verbose_name="Piso de la boca", null=True, blank=True)
    gingival_tissue_condition = models.CharField(max_length=10, choices=[('abnormal', 'Anormal'), ('normal', 'Normal')], default='normal', verbose_name="Tejido gingival – periodontal", null=True, blank=True)
    number_of_teeth = models.IntegerField(default=0, verbose_name="Cantidad de dientes presentes", null=True, blank=True)
    tartar_presence = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="Presencia de sarro", null=True, blank=True)
    periodontal_disease = models.CharField(max_length=3, choices=[('yes', 'Sí'), ('no', 'No')], default='no', verbose_name="Enfermedad periodontal", null=True, blank=True)
    periodontal_disease_location = models.CharField(max_length=200, blank=True, null=True, default='', verbose_name="¿Dónde? (si es localizada)")
    diagnosis = models.TextField(default='', verbose_name="Diagnóstico", null=True, blank=True)
    treatment_plan = models.TextField(default='', verbose_name="Plan de Tratamiento", null=True, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date} {self.time}"