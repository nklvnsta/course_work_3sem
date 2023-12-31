# Generated by Django 4.2.2 on 2023-07-02 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0004_alter_sparepart_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_started', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала гарантии')),
                ('datetime_finished', models.DateTimeField(auto_now=True, verbose_name='Дата окончания гарантии')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Активна'), (1, 'Просрочена'), (2, 'Использована')], default=0, verbose_name='Статус')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device', verbose_name='Устройство')),
            ],
            options={
                'verbose_name': 'Гарантия',
                'verbose_name_plural': 'Гарантии',
            },
        ),
    ]
