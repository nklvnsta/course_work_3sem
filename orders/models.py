from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords

User = get_user_model()

ORDER_STATUS_CHOICES = [
    (1, 'Новый'),
    (2, 'В работе'),
    (3, 'Завершен'),
]


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders',
                                 verbose_name='Заказчик')
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='Статус')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена',
                                help_text='Укажите цену в рублях')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    history = HistoricalRecords()

    def __str__(self):
        return f'Заказ id {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
