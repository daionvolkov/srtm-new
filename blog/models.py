from django.db import models

from django.shortcuts import render


class Bearing(models.Model): # Создаем базу материалов
    code = models.CharField('Артикул', max_length=200)
    description = models.CharField('Описание', max_length=200)
    amaunt = models.IntegerField('Количество')

    def __str__(self):
        return f'Артикул: {self.code}'

    class Meta:
        verbose_name = 'Подшипник'
        verbose_name_plural = 'Подшипники'
