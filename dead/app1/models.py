from django.db import models


class Gifts(models.Model):
    title = models.CharField('Название', max_length=50)
    uurl = models.CharField('Ссылка', max_length=200)
    task = models.ImageField(upload_to='images/')
    whom = models.CharField('Кому', max_length=50)
    age = models.CharField('Возраст', max_length=50)
    reason = models.CharField('Повод', max_length=50)

    def __str__(self):
        return self.title


class Basket(models.Model):
    title = models.CharField('Название', max_length=50)
    uurl = models.CharField('Ссылка', max_length=200)
    task = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

