from django.shortcuts import render
from apps.hello.models import Contact


def index(request):
    contact = Contact.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})
