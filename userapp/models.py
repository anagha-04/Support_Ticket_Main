from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class SupportTicketModel(models.Model):

    user = models.ForeignKey(User,on_delete= models.CASCADE)

    subject = models.CharField(max_length=30)

    message = models.CharField(max_length=40)

    DEPARTMENT_CHOICES =[
        ("technical","TECHNICAL"),
        ("billing","BILLING"),
        ("sales","SALES")
    ]

    department =models.CharField(max_length=30,choices=DEPARTMENT_CHOICES)

    created_at = models.DateField(auto_now_add= True)