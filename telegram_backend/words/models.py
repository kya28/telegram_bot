from django.db import models

class Words(models.Model):
    GENDERS = [
        ('женский', 'Женский'),
        ('мужской', 'Мужской'),
        ('средний', 'Средний'),
    ]
    word = models.CharField(verbose_name='Word', max_length=100)
    gender = models.CharField(verbose_name='Gender', max_length=7, choices=GENDERS)

    def __str__(self):
        return str(self.gender) + ' ' + str(self.word)
