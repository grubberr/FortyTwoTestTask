from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    contact = Contact.objects.filter(email='grubberr@gmail.com').first()
    return render(request, 'hello/index.html', {'contact': contact})
