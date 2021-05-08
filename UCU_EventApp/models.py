from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your models here.

class Member(models.Model):
    TYPES = (
        ('Participant', 'Participant'),
        ('Speaker', 'Speaker'),
    )
    uid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    participant = models.CharField(max_length=150, choices=TYPES,default='Participant')
    topic_to_Present = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    


class Contact(models.Model):
    uid = models.AutoField(primary_key=True)
    fulltname = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=20)
    
    def __str__(self):
        return self.fulltname