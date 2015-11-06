from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    bio = models.TextField()
    other_contacts = models.TextField()
    email = models.EmailField(unique=True)
    jabber = models.EmailField()
    skype = models.CharField(max_length=256)


class Request(models.Model):
    remote_addr = models.GenericIPAddressField()
    date_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    request = models.CharField(max_length=256)
    status_code = models.IntegerField()
