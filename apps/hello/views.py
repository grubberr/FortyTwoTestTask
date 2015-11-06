from django.shortcuts import render
from apps.hello.models import Contact
from apps.hello.utils import get_object_or_none


def index(request):
    contact = get_object_or_none(Contact, email='grubberr@gmail.com')
    return render(request, 'hello/index.html', {'contact': contact})
