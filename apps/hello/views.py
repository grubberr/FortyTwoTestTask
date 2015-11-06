from django.shortcuts import render, get_object_or_404
from apps.hello.models import Contact


def index(request):
    contact = get_object_or_404(Contact, email='grubberr@gmail.com')
    return render(request, 'hello/index.html', {'contact': contact})
