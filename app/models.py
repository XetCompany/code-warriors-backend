from datetime import timedelta, datetime

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CategoryRequest(models.Model):
    """Категория запроса"""
    name = models.CharField(verbose_name='Название категории', max_length=255)

    def get_category_display(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория запроса'
        verbose_name_plural = 'Категории запросов'

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Фотографии"""
    photo = models.ImageField(verbose_name='Фотография', upload_to='photos')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'Фотография {self.id}'


class Video(models.Model):
    """Видео"""
    video = models.FileField(verbose_name='Видео', upload_to='videos')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'Видео {self.id}'


class Response(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to='User', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photos = models.ManyToManyField(verbose_name='Фотографии', to='Photo', blank=True)
    videos = models.ManyToManyField(verbose_name='Видео', to='Video', blank=True)


class Request(models.Model):
    """Сведения о запросе на оказание услуг"""
    creator = models.ForeignKey(verbose_name='Заказчик', to='User',
                                on_delete=models.CASCADE, related_name='creator')
    executor = models.ForeignKey(verbose_name='Исполнитель', to='User', on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name='executor')

    title = models.CharField(verbose_name='Заголовок запроса', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price_from = models.IntegerField(verbose_name='Желаемая цена от', blank=True, null=True)
    price_to = models.IntegerField(verbose_name='Желаемая цена до', blank=True, null=True)
    deadline_in_days = models.IntegerField(verbose_name='Сроки оказания услуг')
    place = models.CharField(verbose_name='Место оказания услуг', max_length=255)
    category = models.ForeignKey(verbose_name='Категория', to='CategoryRequest',
                                 on_delete=models.CASCADE)
    photos = models.ManyToManyField(verbose_name='Фотографии', to='Photo', blank=True)
    videos = models.ManyToManyField(verbose_name='Видео', to='Video', blank=True)

    responses = models.ManyToManyField(verbose_name='Отклики', to='Response', blank=True,
                                       related_name='responses')

    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Когда создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Когда обновлен', auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'id: {self.id}, title: {self.title}'


class Notification(models.Model):
    """Уведомление которое отправляется и отслеживаются прочитал ли пользователь"""
    user = models.ForeignKey(verbose_name='Пользователь', to='User',
                             on_delete=models.CASCADE)
    message = models.CharField(verbose_name='Сообщение', max_length=255)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return f'{self.user.username} <{self.message}>'


class User(AbstractUser):
    """Пользователь способный пройти авторизацию либо регистрацию по логину либо e-mail'у"""
    username = models.CharField(verbose_name='Логин', max_length=255, unique=True)
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    fullname = models.CharField(verbose_name='ФИО', max_length=255, blank=True, null=True)
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True, default=None)
    description = models.TextField(verbose_name='Описание', max_length=255, blank=True, null=True)

    notifications = models.ManyToManyField(verbose_name='Уведомления', to=Notification,
                                           related_name='notification')

    def add_group(self, group_name):
        group = Group.objects.get(name=group_name)
        self.groups.add(group)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'id: {self.id}, log: {self.username}'


class ResetPasswordToken(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to='User',
                             on_delete=models.CASCADE)
    token = models.CharField(verbose_name='Токен', unique=True, max_length=255)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)

    # TODO: сделать удаление токена через 1 час

    def is_expired(self):
        future_time = self.created_at + timedelta(hours=1)
        now_time = datetime.now(tz=None) - timedelta(hours=3)
        # TODO: костыль
        now_time = now_time.replace(tzinfo=None)
        future_time = future_time.replace(tzinfo=None)
        return now_time > future_time

    def is_valid(self):
        return not self.is_expired()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Токен для сброса пароля'
        verbose_name_plural = 'Токены для сброса пароля'

    def __str__(self):
        return f'id: {self.id}, user: {self.user.username}'
