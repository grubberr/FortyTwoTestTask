from django.contrib import admin
from apps.hello.models import Contact, Request


admin.site.register(Contact)
admin.site.register(Request)
