from django.db import models

from django.utils import timezone

from enum import Enum
from actions.models import User


class Categories(models.Model):
    category = models.CharField(max_length=30)
    picture = models.ImageField(blank=True, null=True, upload_to='static/img/')

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
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=30, choices=TaskStatus.get_choices(), default='looking for executor')
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Categories, related_name='categories', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Offers(models.Model):
    suggested_by = models.ForeignKey(User, related_name='suggested_by', on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, related_name='task', on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    posted_time = models.DateTimeField(auto_now_add=True, blank=True)


class Comments(models.Model):
    for_whom = models.PositiveIntegerField()
    from_whom = models.PositiveIntegerField()
    text = models.CharField(max_length=500, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_positive = models.BooleanField()
