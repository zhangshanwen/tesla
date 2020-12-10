from django.db import models
import time


class Base(models.Model):
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_deleted = models.BooleanField(default=0)

    def __init__(self, *args, **kwargs):
        for k in list(kwargs.keys()):
            if hasattr(self, k):
                self.__dict__[k] = kwargs[k]
            else:
                kwargs.pop(k)
        super().__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        now = int(time.time())
        self.created_at = self.created_at if self.created_at else now
        self.updated_at = now
        super(Base, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        abstract = True
