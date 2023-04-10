from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Request(models.Model):
    """Сведения о запросе на оказание услуг"""

    creator = models.ForeignKey(verbose_name='Заказчик', to='User',
                                on_delete=models.SET_NULL, null=True, related_name='creator')
    executor = models.ForeignKey(verbose_name='Исполнитель', to='User',
                                 on_delete=models.SET_NULL, null=True, related_name='executor')

    title = models.CharField(verbose_name='Заголовок запроса', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price_from = models.IntegerField(verbose_name='Желаемая цена от', blank=True, null=True)
    price_to = models.IntegerField(verbose_name='Желаемая цена до', blank=True, null=True)
    deadline_in_days = models.IntegerField(verbose_name='Сроки оказания услуг')
    place = models.CharField(verbose_name='Место оказания услуг', max_length=255)

    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Когда создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Когда обновлен', auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.title


class Notification(models.Model):
    """Уведомления которая отправляет сообщения и отслеживания прочитал ли пользователь"""
    user = models.ForeignKey(verbose_name='Пользователь', to='User',
                             on_delete=models.CASCADE,)
    message = models.CharField(verbose_name='Сообщение', max_length=255)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return self.message

class User(AbstractUser):
    """Пользователь способный пройти авторизацию либо регистрацию по логину либо e-mail'у"""
    username = models.CharField(verbose_name='Логин', max_length=255, unique=True)
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    fullname = models.CharField(verbose_name='ФИО', max_length=255, blank=True, null=True)
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', max_length=255, blank=True, null=True)

    notifications = models.ManyToManyField(verbose_name='Уведомления', to=Notification,
                                           related_name='notification')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'id: {self.id}, log: {self.username}'