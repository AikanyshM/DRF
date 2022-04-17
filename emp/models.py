from django.db import models

class Position(models.Model):
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.position

class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.CharField(max_length=6)

    def __str__(self):
        return self.position
