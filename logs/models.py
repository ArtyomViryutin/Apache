from django.db import models
from datetime import datetime


class Log(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateTimeField()
    method = models.CharField(max_length=7)
    uri = models.TextField()
    status = models.PositiveSmallIntegerField()
    response_size = models.IntegerField()

    def __str__(self):
        return self.ip + datetime.strftime(self.date, '%d.%m.%Y %H:%M:%S')

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
