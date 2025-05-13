from django.db import models

class Meter(models.Model):
    meter_number = models.CharField(max_length=50, unique=True)
    current_day_reading = models.IntegerField(default=0)
    current_night_reading = models.IntegerField(default=0)

    def __str__(self):
        return f"Meter {self.meter_number} - Day: {self.current_day_reading}, Night: {self.current_night_reading}"

class MeterReading(models.Model):
    meter_number = models.CharField(max_length=50)
    day_reading = models.IntegerField()
    night_reading = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meter {self.meter_number} - Day: {self.day_reading}, Night: {self.night_reading}"

class Tariff(models.Model):
    day_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    night_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)

    def __str__(self):
        return f"Day: {self.day_rate}, Night: {self.night_rate}"

class Bill(models.Model):
    meter_number = models.CharField(max_length=50)
    day_kwh = models.IntegerField()
    night_kwh = models.IntegerField()
    day_rate = models.DecimalField(max_digits=5, decimal_places=2)
    night_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bill for Meter {self.meter_number} on {self.date_created}"
