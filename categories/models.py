from django.db import models

from datetime import datetime
from enum import Enum


class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class TaskStatus(Enum):
    looking_for_executor = 'Looking for executor'
    in_process = 'In process'
    done = 'Done'

    @classmethod
    def get_choices(cls):
        return [
            (el.value, name)
            for name, el in cls.__members__.items()
        ]


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=30, choices=TaskStatus.get_choices(), default='looking for executor')
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
