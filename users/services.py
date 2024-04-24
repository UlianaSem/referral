import logging
import random
import string
import time

from rest_framework import status
from rest_framework.authtoken.models import Token

from users import models


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AuthUser:

    def __init__(self, phone):
        self.phone = phone

    def _check_user(self):
        return models.User.objects.filter(phone=self.phone).exists()

    def get_code(self):
        if self._check_user():
            user = models.User.objects.get(phone=self.phone)

        else:
            user = models.User.objects.create(
                phone=self.phone,
                own_code=self._generate_code(6, f'{string.ascii_letters}{string.digits}')
            )
        user.verification_code = self._generate_code()
        user.save()

        logger.info(f'Пользователь {user}: проверочный код - {user.verification_code},'
                    f' личный инвайт-код: {user.own_code}')

        time.sleep(2)

        return {
            'status': status.HTTP_200_OK,
            'message': 'Code sent'
        }

    def check_code(self, code):
        if self._check_user():
            user = models.User.objects.get(phone=self.phone)

            if user.verification_code == code:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                return {
                    'status': status.HTTP_200_OK,
                    'message': 'Token sent',
                    'token': token.key
                }

        return {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Token not sent'
        }

    @staticmethod
    def _generate_code(size=4, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))
