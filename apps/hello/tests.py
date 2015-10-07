import datetime
from django.test import TestCase
from apps.hello.models import Contact

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)

    def test_my_contact(self):
        "put docstrings in your tests"
        contact = Contact.objects.get()
        assert(contact.name == 'Sergey')
        assert(contact.surname == 'Chvalyuk')
        assert(contact.date_of_birth == datetime.date(1981, 9, 19))
