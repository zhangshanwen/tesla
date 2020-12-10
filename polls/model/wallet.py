from django.db import models
from .base import Base
from polls.codes.common import *


class Wallet(Base):
    user_id = models.IntegerField(max_length=10)
    balance = models.IntegerField(max_length=16)

    def create(self):
        if Wallet.objects.filter(user_id=self.user_id, is_deleted=0):
            return CodeStatus.wallet_exist
        self.save()