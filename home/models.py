from django.db import models


# Create your models here.
class Tasks(models.Model):
    Taskname = models.CharField(max_length=300)

    def __str__(self):
        return self.Taskname[:50]
