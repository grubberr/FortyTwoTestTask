import datetime
from django.test import TestCase
from apps.hello.models import Contact
from django.core.urlresolvers import reverse

# Create your tests here.


class SomeTests(TestCase):
    fixtures = ['initial_data.json']

    def test_my_contact(self):
        "test data"

        self.assertEqual(len(Contact.objects.all()), 1)

        contact = Contact.objects.get()
        self.assertEqual(contact.name, 'Sergey')
        self.assertEqual(contact.surname, 'Chvalyuk')
        self.assertEqual(contact.date_of_birth, datetime.date(1981, 9, 19))
        self.assertEqual(contact.email, 'grubberr@gmail.com')
        self.assertEqual(contact.skype, 'sergey_ant')

    def test_web(self):
        " test web "

        contact = Contact.objects.get(email='grubberr@gmail.com')
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, contact.name, 2)
        self.assertContains(response, contact.surname, 2)
        self.assertContains(response, contact.bio, 1)
        self.assertContains(response, contact.other_contacts, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.jabber, 1)
        self.assertContains(response, contact.skype, 1)

    def test_admin(self):
        " test admin accessible "

        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

        data = {'name': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('admin:index'), data)
        self.assertEqual(response.status_code, 200)

    def test_empty(self):
        " test empty "

        Contact.objects.all().delete()
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 404)
