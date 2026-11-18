from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class User(AbstractUser):
    pass

class Speciality(models.Model):
    name = models.CharField(max_length=100)

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    specialties = models.ManyToManyField('Speciality', related_name='doctors')

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[RegexValidator(
        r"^\d{8}$", message="La CIN doit contenir 8 chiffres.")])
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()


# Create your models here.
