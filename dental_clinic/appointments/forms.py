from django import forms
from .models import Appointment, Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'appointment_date', 'time', 'reason']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name', 'email', 'phone', 'next_appointment', 'age', 'birth_date', 'identity_number', 'gender', 'origin', 
            'neighborhood', 'responsible_name', 'relationship', 'responsible_phone', 'hospitalized_last_2_years', 
            'hospitalization_reason', 'under_medical_treatment', 'medical_condition', 'allergic_to_substances', 
            'allergies_detail', 'regular_medications', 'smokes', 'cigarettes_per_day', 'drinks_alcohol', 'alcohol_amount', 
            'is_pregnant', 'pregnancy_months', 'conditions', 'observations', 'attach_medical_report', 'difficulty_speaking', 
            'difficulty_chewing', 'difficulty_opening_mouth', 'difficulty_swallowing', 'bleeding_gums', 'tooth_mobility', 
            'pus_in_mouth', 'pus_location', 'brushing_frequency', 'oral_hygiene_status', 'tongue_condition', 'lips_condition', 
            'cheeks_condition', 'floor_of_mouth_condition', 'gingival_tissue_condition', 'number_of_teeth', 'tartar_presence', 
            'periodontal_disease', 'periodontal_disease_location', 'diagnosis', 'treatment_plan'
        ]
        widgets = {
            'conditions': forms.CheckboxSelectMultiple,
            'birth_date': forms.SelectDateWidget(years=range(1900, 2025)),
        }