from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from apps.hello.models import Contact, Request


def index(request):
    contact = Contact.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def requests(request):
    records = Request.objects.order_by('-date_time')[:10]
    if request.is_ajax():
        data = serializers.serialize('json', records)
        return HttpResponse(data, content_type='application/json')
    return render(request, 'hello/requests.html', {'records': records})
