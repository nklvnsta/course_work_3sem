from django.db import models
from simple_history.models import HistoricalRecords

class SparePart(models.Model):
    name = models.TextField(max_length=512,
                            verbose_name='Название')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена',
                                help_text='Укажите цену в рублях')
    delivery_time = models.PositiveSmallIntegerField(verbose_name='Время доставки')
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.TextField(max_length=512,
                            verbose_name='Название')
    model = models.TextField(max_length=512, verbose_name='Модель')
    serial_number = models.TextField(max_length=512,
                                     verbose_name='Серийный номер')
    purchase_date = models.DateField(verbose_name='Дата покупки')
    warranty_expiration_date = models.DateField(verbose_name='Дата окончания гарантии')

    spare_parts = models.ManyToManyField(SparePart, related_name='devices', verbose_name='Запчасти')
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return self.name