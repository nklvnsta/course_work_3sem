from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.validators import phone_validator

User = get_user_model()


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile",
                                verbose_name="Пользователь")
    patronymic = models.TextField(blank=True, null=True, verbose_name="Отчество")
    phone_number = models.CharField(validators=[phone_validator], max_length=17, blank=True, null=True,
                                    verbose_name="Номер телефона")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")

    
    class Meta:
        verbose_name = "Поля клиента"
        verbose_name_plural = "Поля клиента"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile",
                                verbose_name="Пользователь")
    patronymic = models.TextField(blank=True, null=True, verbose_name="Отчество")
    birthday = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    position = models.TextField(blank=True, null=True, verbose_name="Должность")
    salary = models.PositiveIntegerField(blank=True, null=True,
                                         default=50000,
                                         verbose_name="Зарплата",
                                         help_text="в рублях")

    class Meta:
        verbose_name = "Поля сотрудников"
        verbose_name_plural = "Поля сотрудников"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, "customer_profile"):
        CustomerProfile.objects.create(user=instance)
    instance.customer_profile.save()

    if created or not hasattr(instance, "staff_profile"):
        StaffProfile.objects.create(user=instance)
    instance.staff_profile.save()
