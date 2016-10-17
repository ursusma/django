from django.db import models
from django.utils import timezone

# Create your models here.

class Rank(models.Model):
    RankID = models.TextField()
    RankName = models.CharField(max_length=64)
    RankWeb = models.TextField()

    def __str__(self):
        return self.RankName

class Status(models.Model):
    idlestat = models.TextField(default="")
    systime = models.TextField()
    usersnumber = models.TextField()
    loadavg = models.TextField()
    cpufree = models.TextField()
    memoryfree = models.TextField()
