from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Task(models.Model):
    task_name = models.CharField(max_length=225)
    isDone = models.BooleanField(default=False)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.task_name


class Person(models.Model):
    first_name = models.CharField(max_length=225, null=False)
    last_name = models.CharField(max_length=225, null=False)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    salary = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    isfired = models.BooleanField(default=False)
    ispresent = models.BooleanField(default=False)
    onBreak = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Annoucement(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
