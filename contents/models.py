from django.utils import timezone
from django.db import models

from hashlib import md5
import os



def image_rename(instance, filename):
    name = md5(f'{timezone.now()}'.encode()).hexdigest()
    ext = os.path.splitext(filename)[-1]

    return f'{timezone.now():%Y/%m/%d}/{name}{ext}'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(upload_to=image_rename, verbose_name='Картинка')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')

    HASHTAGS = (
        ('n', '#новости'),
        ('t', '#техосмотр'),
        ('p', '#покраска'),
        ('r', '#ремонт'),
        ('a', '#советы'),
        ('h', '#юмор'),
    )

    hashtag = models.CharField(max_length=1, choices=HASHTAGS, blank=True, default='n', verbose_name='Хештег',
        help_text='Данная функция не работает, сделано в расчете на будущие изменения.')

    views = models.IntegerField(default=0, verbose_name='Просмотры')
    comments = models.IntegerField(default=0, verbose_name='Комментарии')

    close = models.BooleanField(default=False, verbose_name='Закрыть тему',
        help_text='Закрыв тему, отключается возможность оставлять комментарии.')


    class Meta:
        verbose_name_plural = ('Новости')
        verbose_name = ('Новость')


    def __str__(self):
        return self.title
