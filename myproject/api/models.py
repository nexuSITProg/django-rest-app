# tutors/models.py

from django.db import models

class Subject(models.Model):
    subject_id = models.CharField(max_length=50, primary_key=True)
    subject_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return self.subject_name


class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    experience = models.PositiveIntegerField()
    bio = models.TextField(blank=True)

    class Meta:
        db_table = 'tutors'

    def __str__(self):
        return f"{self.name} {self.second_name} {self.last_name}"


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    ]
    id = models.AutoField(primary_key=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'schedule'

    def __str__(self):
        return f"{self.tutor.name} {self.day_of_week} {self.start_time}-{self.end_time}"
    

class Records(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    tutor_id = models.IntegerField()

    class Meta: 
        db_table = 'records'

    def __str__(self):
        return f"{self.fio} {self.phone}"