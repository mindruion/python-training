from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Debitor(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=Gender.choices)
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(10)])
    is_good = models.BooleanField(default=False)
    birthday = models.DateTimeField(null=True)


