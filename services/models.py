from django.db import models

from simple_history.models import HistoricalRecords

class Service(models.Model):
    name = models.TextField(max_length=512,
                            verbose_name='Название')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена',
                                help_text='в рублях',
                                )

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
