import datetime
from django.test import TestCase
from apps.hello.models import Contact

# Create your tests here.


class SomeTests(TestCase):

    def test_my_contact(self):
        "test data"

        self.assertEqual(len(Contact.objects.all()), 1)

        contact = Contact.objects.get()
        self.assertEqual(contact.name, 'Sergey')
        self.assertEqual(contact.surname, 'Chvalyuk')
        self.assertEqual(contact.date_of_birth, datetime.date(1981, 9, 19))

    def test_web(self):
        " test web "

        response = self.client.get('/')
        self.assertEqual(response.status_code, 301)
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content.find('Sergey') > -1)
        self.assertTrue(response.content.find('Chvalyuk') > -1)
