from django.contrib.auth.models import AbstractUser
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=100)
    is_access = models.BooleanField(default=False)
    main_employ = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    fio = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    vkontakte = models.URLField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, blank=True)
    department_access = models.ForeignKey('Department', related_name='access', on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(null=True)
    experience = models.PositiveIntegerField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return self.fio


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey('SensorType', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SensorType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class MapRooms(models.Model):
    name = models.CharField(max_length=100,  default='', blank=True)
    level = models.IntegerField()
    coordinates_json = models.JSONField()
    
    def __str__(self):
        return str(self.name) + " | " + str(self.id) 

class MapIcons(models.Model):
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name

class MapPoint(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ForeignKey(MapIcons, on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField()
    coordinates_json = models.JSONField()

    def __str__(self):
        return self.name

