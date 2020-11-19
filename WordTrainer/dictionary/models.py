from django.db import models
from django.contrib.auth.models import User


class Dictionary(models.Model):
    dictionary_name = models.CharField(max_length=255, verbose_name="Название словаря")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец словаря")
    data_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    def __str__(self):
        return self.dictionary_name

    class Meta:
        ordering = ('dictionary_name',)
        verbose_name = 'Словарь'
        verbose_name_plural = 'Словари'


class Word(models.Model):
    native_meaning = models.CharField(max_length=255, verbose_name="Значение на родном языке")
    foreign_meaning = models.CharField(max_length=255, verbose_name="Значение на иностранном языке")
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="Словарь")

    def __str__(self):
        return self.native_meaning + ' ' + self.foreign_meaning + ' - словарь: ' + self.dictionary.dictionary_name

    class Meta:
        ordering = ('dictionary',)
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'



