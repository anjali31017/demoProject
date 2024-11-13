from django.db import models
from django.contrib.auth.models import AbstractUser 

class newAdmission(AbstractUser):
    COURSE_CATEGORY = [
        ('CS','Computer Science'),
        ('IT','Information Technology'),
        ('CA', 'Computer Applications')
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    percent_12 = models.DecimalField(max_digits=4, blank=True)
    course = models.CharField(max_length=30,choices=COURSE_CATEGORY, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email