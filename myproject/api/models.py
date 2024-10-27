# tutors/models.py

from django.db import models

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'subjects'  # Это изменит имя таблицы

    def __str__(self):
        return self.subject_name
    
class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    experience = models.IntegerField()
    bio = models.TextField()
    
    class Meta:
        db_table = 'tutors'  # Это изменит имя таблицы
    
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]
    schedule_id = models.AutoField(primary_key=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=11, choices=DAYS_OF_WEEK)  # Дни недели могут быть до 9 символов
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'schedule'  # Это изменит имя таблицы

    def __str__(self):
        return f'{self.tutor.name} {self.day_of_week} {self.start_time}-{self.end_time}'