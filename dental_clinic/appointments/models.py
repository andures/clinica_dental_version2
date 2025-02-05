from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils import timezone

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

    ToothCondition =[
         ('S', 'S'),# ('S', 'Sano (S)'),
        ('A', 'A'), #('A', 'Amalgama (A)'),
        ('R', 'R'),#('R', 'Resina (R)'),
        ('C', 'C'),#('C', 'Caries (C)'),
        ('-', '-'),#('-', 'Ausente (-)'),
        ('X', 'X'),# ('X', 'Perdido (X)'),
        ('EI', 'EI'), #('EI', 'Extracción Indicada (EI)'),
        ('P', 'P'), #('P', 'Periodontopatias (P)'),
        ('E', 'E'), #('E', 'Endodoncia (E)'),
        ('PR', 'PR'), #('PR', 'Prótesis Removible (PR)'),
        ('I', 'I'), #('I', 'Incrustación (I)'),
        ('FR', 'FR'), #('FR', 'Fractura Dentaria (FR)'),
        ('S', 'S'), #('S', 'Sellantes (S)'),
        ('PP', 'PP'), #('PP', 'Pulpotomía (PP)'),
        ('PC', 'PC'), #('PC', 'Pulpectomia (PC)'),
    ]

    CONDITIONS_TYPE_CHOICES = [
        ('generalized', 'Generalizada'),
        ('localized', 'Localizada')
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
    conditions_type = models.CharField(max_length=20, choices=CONDITIONS_TYPE_CHOICES, default='generalized', verbose_name="Tipo de afección", null=True, blank=True)
    #tooth_condition models grupal
    tooth_1 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 1")
    tooth_2 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 2")
    tooth_3 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 3")
    tooth_4 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 4")
    tooth_5 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 5")
    tooth_6 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 6")
    tooth_7 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 7")
    tooth_8 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 8")
    tooth_9 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 9")
    tooth_10 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 10")
    tooth_11 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 11")
    tooth_12 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 12")
    tooth_13 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 13")
    tooth_14 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 14")
    tooth_15 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 15")
    tooth_16 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 16")
    tooth_17 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 17")
    tooth_18 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 18")
    tooth_19 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 19")
    tooth_20 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 20")
    tooth_21 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 21")
    tooth_22 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 22")
    tooth_23 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 23")
    tooth_24 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 24")
    tooth_25 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 25")
    tooth_26 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 26")
    tooth_27 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 27")
    tooth_28 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 28")
    tooth_29 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 29")
    tooth_30 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 30")
    tooth_31 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 31")
    tooth_32 = models.CharField(max_length=2, choices=ToothCondition, blank=True, null=True, verbose_name="Diente 32")
    #tooth_condition models grupal
    diagnosis = models.TextField(default='', verbose_name="Diagnóstico", null=True, blank=True)
    treatment_plan = models.TextField(default='', verbose_name="Plan de Tratamiento", null=True, blank=True)

    @property
    def next_appointment(self):
        return self.appointments.filter(appointment_date__gte=timezone.now()).order_by('appointment_date').first()
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    time = models.TimeField()
    reason = models.TextField()
    dentist = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField(default='', verbose_name="Correo Electrónico", null=True, blank=True)
    is_completed = models.BooleanField(default=False, verbose_name="¿Está completado?")

    def save(self, *args, **kwargs):
        self.email = self.patient.email
        super(Appointment, self).save(*args, **kwargs)
        self.patient.next_appointment = self.patient.next_appointment_date
        self.patient.save()
        
    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date} {self.time}"

class Budget(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.TextField(verbose_name="Tratamiento")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo")
    is_paid = models.BooleanField(default=False, verbose_name="¿Está pagado?")
    is_completed = models.BooleanField(default=False, verbose_name="¿Está completado?")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"{self.patient.name} - {self.treatment} - {self.cost}"