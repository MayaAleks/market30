from django.db import models

# Create your models here.
class Person(models.Model):
    nickname = models.CharField(max_length=30, verbose_name='Никнейм')
    login = models.CharField(max_length=30, verbose_name='Логин', unique=True)
    password = models.CharField(max_length=30,verbose_name='Пароль')
    avatar = models.ImageField(upload_to='image_person', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Пользователь'
