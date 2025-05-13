from django import forms
from .models import MeterReading, Tariff

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['meter_number', 'day_reading', 'night_reading']
        labels = {
            'meter_number': 'Номер лічильника',
            'day_reading': 'Показник день',
            'night_reading': 'Показник ніч',
        }

class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['day_rate', 'night_rate']
        labels = {
            'day_rate': 'Тариф "день"',
            'night_rate': 'Тариф "ніч"',
        }