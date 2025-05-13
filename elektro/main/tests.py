from django.test import TestCase
from django.urls import reverse
from .models import Meter, MeterReading, Tariff, Bill

class MeterReadingTests(TestCase):
    def setUp(self):
        # Створення тестових даних
        self.tariff = Tariff.objects.create(day_rate=1.50, night_rate=1.00)
        self.meter = Meter.objects.create(meter_number="12345", current_day_reading=10, current_night_reading=15)

    def test_submit_reading_success(self):
        # Тест успішного подання показників
        response = self.client.post(reverse('submit_reading'), {
            'meter_number': '12345',
            'day_reading': 12,
            'night_reading': 18,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Показники успішно збережено!")

        # Перевірка оновлення показників
        meter = Meter.objects.get(meter_number="12345")
        self.assertEqual(meter.current_day_reading, 12)
        self.assertEqual(meter.current_night_reading, 18)

        # Перевірка створення рахунку
        bill = Bill.objects.get(meter_number="12345")
        self.assertEqual(bill.day_kwh, 2)  # 12 - 10
        self.assertEqual(bill.night_kwh, 3)  # 18 - 15
        self.assertEqual(bill.total_cost, 2 * 1.50 + 3 * 1.00)

    def test_submit_reading_lower_values_day(self):
        # Тест подання показників, менших за попередні
        response = self.client.post(reverse('submit_reading'), {
            'meter_number': '12345',
            'day_reading': 8,
            'night_reading': 14,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нові денні показники не можуть бути меншими за попередні.")

    def test_submit_reading_lower_values_night(self):
        # Тест подання показників, менших за попередні
        response = self.client.post(reverse('submit_reading'), {
            'meter_number': '12345',
            'day_reading': 20,
            'night_reading': 14,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нові нічні показники не можуть бути меншими за попередні.")

    def test_new_meter_creation(self):
        # Тест створення нового лічильника
        response = self.client.post(reverse('submit_reading'), {
            'meter_number': '67890',
            'day_reading': 5,
            'night_reading': 7,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Показники успішно збережено!")

        # Перевірка створення нового лічильника
        meter = Meter.objects.get(meter_number="67890")
        self.assertEqual(meter.current_day_reading, 5)
        self.assertEqual(meter.current_night_reading, 7)

    def test_tariff_update(self):
        # Тест оновлення тарифів
        response = self.client.post(reverse('tariffs'), {
            'day_rate': 2.00,
            'night_rate': 1.50,
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного збереження

        # Перевірка оновлення тарифів
        tariff = Tariff.objects.get(id=1)
        self.assertEqual(tariff.day_rate, 2.00)
        self.assertEqual(tariff.night_rate, 1.50)

    def test_meters_page(self):
        # Тест сторінки лічильників
        response = self.client.get(reverse('meters'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "12345")
        self.assertContains(response, "10")  # Поточний показник день
        self.assertContains(response, "15")  # Поточний показник ніч

    def test_bills_page(self):
        # Тест сторінки рахунків
        Bill.objects.create(
            meter_number="12345",
            day_kwh=2,
            night_kwh=3,
            day_rate=1.50,
            night_rate=1.00,
            total_cost=6.00
        )
        response = self.client.get(reverse('bills'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "12345")
        self.assertContains(response, "2")  # КВт за день
        self.assertContains(response, "3")  # КВт за ніч
        self.assertContains(response, "6.00")  # Загальна вартість
