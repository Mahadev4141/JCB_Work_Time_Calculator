from django.db import models
from django.contrib.auth.models import User


class WorkRecord(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    date = models.DateField()
    operator = models.CharField(max_length=100)
    machine = models.CharField(max_length=50)
    site = models.CharField(max_length=100)

    start_time = models.TimeField()
    end_time = models.TimeField()

    total_time = models.CharField(max_length=50)
    break_time = models.CharField(max_length=50)
    working_time = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.operator