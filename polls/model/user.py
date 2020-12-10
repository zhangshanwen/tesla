from django.db import models
from .base import Base
from polls.codes.common import *


class User(Base):
    mobile = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def create(self):
        if User.objects.filter(mobile=self.mobile, is_deleted=0):
            return CodeStatus.mobile_exist
        self.save()