from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    bio = models.TextField()
    other_contacts = models.TextField()
    email = models.EmailField(unique=True)
    jabber = models.EmailField()
    skype = models.CharField(max_length=256)
