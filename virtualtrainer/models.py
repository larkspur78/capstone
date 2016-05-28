from django.db import models

# Create your models here.


class MuscleGroup(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    video = models.URLField()
    musclegroup = models.ForeignKey(MuscleGroup)

    def __str__(self):
        return self.name
