from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)


class Review(models.Model):
    CHOICES = (
        ('first', '1 курс'),
        ('second', '2 курс'),
        ('third', '3 курс'),
        ('fourth', '4 курс'),
    )
    username = models.CharField(max_length=50)
    course = models.CharField(max_length=200, choices=CHOICES)
    teacherOrCourse = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()

    
    
class Advice(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()

