from django.db import models

# Create your models here.


NEW = 1
APPROVED = 2
CANCELLED = 3
FINISHED = 4


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    com_name = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=200)
    com_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    time_limit = models.IntegerField()

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=200)
    worker_name = models.OneToOneField(
        Worker, on_delete=models.CASCADE, primary_key=True
        )
    work_name = models.ForeignKey(Work, on_delete=models.CASCADE)
    choice = [
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
        ]
    status = models.IntegerField(choices=choice)

    def __str__(self):
        return self.name


class WorkTime(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    choice = [
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
        ]
    status = models.IntegerField(choices=choice, default=NEW)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    hours_worked = models.IntegerField()


class Statistic(models.Model):
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)
    hours_worked = models.IntegerField()
    record_date = models.DateTimeField(auto_now_add=True)
