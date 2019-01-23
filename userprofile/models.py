from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

from datetime import date



class Profile(models.Model):
    SEX = (
        ('n', 'Не сообщаю'),
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    EXPERIENCE = (
        ('e', 'Начинающий'),
        ('m', 'Любитель'),
        ('h', 'Профессионал'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=date(1969, 1, 3), verbose_name='День рождения')
    place = models.CharField(max_length=16, blank=True, verbose_name='Место жительства')
    sex = models.CharField(max_length=1, choices=SEX, default='n', verbose_name='Пол')
    experience = models.CharField(max_length=1, choices=EXPERIENCE, default='e', verbose_name='Уровень вождения')
    about = models.TextField(max_length=700, blank=True, verbose_name='О себе')
    comments = models.IntegerField(default=0, verbose_name='Комментарии')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
