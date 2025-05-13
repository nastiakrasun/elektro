from django.shortcuts import render, redirect
from django.contrib import messages 
from django.db.models import Sum
from .models import Tariff, Bill, Meter
from .forms import MeterReadingForm, TariffForm

def submit_reading(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)

            meter, created = Meter.objects.get_or_create(meter_number=reading.meter_number)

            if reading.day_reading < meter.current_day_reading:
                messages.error(request, "Нові денні показники не можуть бути меншими за попередні.")
                return render(request, 'main/index.html', {'form': form})

            if reading.night_reading < meter.current_night_reading:
                messages.error(request, "Нові нічні показники не можуть бути меншими за попередні.")
                return render(request, 'main/index.html', {'form': form})

            day_difference = reading.day_reading - meter.current_day_reading
            night_difference = reading.night_reading - meter.current_night_reading

            tariff = Tariff.objects.first()
            if not tariff:
                tariff = Tariff.objects.create(day_rate=1.50, night_rate=1.00)

            day_cost = day_difference * tariff.day_rate
            night_cost = night_difference * tariff.night_rate
            total_cost = day_cost + night_cost

            Bill.objects.create(
                meter_number=reading.meter_number,
                day_kwh=day_difference,
                night_kwh=night_difference,
                day_rate=tariff.day_rate,
                night_rate=tariff.night_rate,
                total_cost=total_cost
            )

            meter.current_day_reading = reading.day_reading
            meter.current_night_reading = reading.night_reading
            meter.save()

            reading.save()

            messages.success(request, "Показники успішно збережено!")

            form = MeterReadingForm() 
        else:
            messages.error(request, "Будь ласка, виправте помилки у формі.")
    else:
        form = MeterReadingForm()
    return render(request, 'main/index.html', {'form': form})

def success(request):
    return render(request, 'main/success.html')

def tariffs(request):
    tariff, created = Tariff.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = TariffForm(request.POST, instance=tariff)
        if form.is_valid():
            form.save()
            return redirect('tariffs')
    else:
        form = TariffForm(instance=tariff)

    return render(request, 'main/tariffs.html', {'form': form, 'tariff': tariff})

def bills(request):
    all_bills = Bill.objects.all().order_by('-date_created')
    return render(request, 'main/bills.html', {'bills': all_bills})

def meters(request):
    meters = Meter.objects.all()

    meter_data = []
    for meter in meters:
        total_cost = Bill.objects.filter(meter_number=meter.meter_number).aggregate(Sum('total_cost'))['total_cost__sum'] or 0
        meter_data.append({
            'meter_number': meter.meter_number,
            'current_day_reading': meter.current_day_reading,
            'current_night_reading': meter.current_night_reading,
            'total_cost': total_cost
        })

    return render(request, 'main/meters.html', {'meters': meter_data})