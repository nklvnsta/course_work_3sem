# Generated by Django 4.2.2 on 2023-06-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_sparepart'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='spare_parts',
            field=models.ManyToManyField(related_name='devices', to='devices.sparepart', verbose_name='Запчасти'),
        ),
    ]
