from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=12, verbose_name='Телефон', unique=True)
    verification_code = models.CharField(max_length=4, verbose_name='Проверочный код',
                                         **NULLABLE)
    own_code = models.CharField(max_length=6, verbose_name='Личный инвайт-код', unique=True)
    entered_code = models.CharField(max_length=6, verbose_name='Введенный инвайт-код',
                                    **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'
