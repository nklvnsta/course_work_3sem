from django.db import models

from devices.models import Device

from simple_history.models import HistoricalRecords

class Guarantee(models.Model):
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               null=False, blank=False,
                               verbose_name="Устройство")
    datetime_started = models.DateTimeField(verbose_name="Дата начала гарантии")
    datetime_finished = models.DateTimeField(verbose_name="Дата окончания гарантии")
    status = models.PositiveSmallIntegerField(default=0, verbose_name="Статус", choices=(
        (0, "Активна"),
        (1, "Просрочена"),
        (2, "Использована"),
    ))
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Гарантия"
        verbose_name_plural = "Гарантии"

    def __str__(self):
        return f"Гарантия {self.pk} на {self.device.name}"
