from django.shortcuts import render
from apps.hello.models import Contact

# Create your views here.


def index(request):
    contact = Contact.objects.get()
    return render(request, 'hello/index.html', {'contact': contact})
