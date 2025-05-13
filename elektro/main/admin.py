from django.contrib import admin
from .models import MeterReading, Tariff, Meter, Bill

admin.site.register(MeterReading)
admin.site.register(Tariff)
admin.site.register(Meter)
admin.site.register(Bill)