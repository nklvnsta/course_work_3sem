from django.db import models

from simple_history.models import HistoricalRecords

class News(models.Model):
    title = models.TextField(
        null=False,
        blank=False,
        verbose_name="Заголовок",
    )
    text = models.TextField(null=False, blank=False, verbose_name="Текст")
    datetime_updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.pk} {self.title}"
