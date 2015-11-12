# -*- coding: utf-8 -*-

import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Contact


class HelloAppTests(TestCase):
    fixtures = ['initial_data.json']

    def test_my_contact_in_database(self):
        " test that in fixtures only one my personal contact "

        self.assertEqual(len(Contact.objects.all()), 1)

        contact = Contact.objects.get()
        self.assertEqual(contact.name, 'Sergey')
        self.assertEqual(contact.surname, 'Chvalyuk')
        self.assertEqual(contact.date_of_birth, datetime.date(1981, 9, 19))
        self.assertEqual(contact.email, 'grubberr@gmail.com')
        self.assertEqual(contact.skype, 'sergey_ant')

    def test_my_contact_in_web(self):
        " test that web page shows my personal contact "

        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sergey', 2)
        self.assertContains(response, 'Chvalyuk', 2)
        self.assertContains(response, 'grubberr@gmail.com', 1)
        self.assertContains(response, 'grubberr@jabber.com', 1)
        self.assertContains(response, 'sergey_ant', 1)

    def test_multi_database_records(self):
        " test that web page shows the first record from database "

        Contact.objects.create(
            name='John',
            surname='Smith',
            email='john@domain.com',
            date_of_birth=datetime.date(2000, 1, 1),
            jabber='jabber@domain.com',
            skype='skype_id')

        self.assertEqual(len(Contact.objects.all()), 2)

        contact = Contact.objects.first()
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, contact.name, 2)
        self.assertContains(response, contact.surname, 2)
        self.assertContains(response, contact.bio, 1)
        self.assertContains(response, contact.other_contacts, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.jabber, 1)
        self.assertContains(response, contact.skype, 1)

    def test_not_found(self):
        "test web page shows 'not found' if database is empty"

        Contact.objects.all().delete()
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Business Card Not Found', 2)

    def test_unicode(self):
        """
        test that we can store contact with unicode characters
        and see it on web page
        """

        Contact.objects.all().delete()

        Contact.objects.create(
            name=u'Джон',
            surname=u'Смит',
            date_of_birth=datetime.date(2000, 1, 1),
            email='john@domain.com')

        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Джон', 2)
        self.assertContains(response, u'Смит', 2)

    def test_admin(self):
        " test admin accessible "

        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

        data = {'name': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('admin:index'), data)
        self.assertEqual(response.status_code, 200)

    def test_auth_admin(self):
        " test if admin / admin exists "
        self.assertTrue(self.client.login(username='admin', password='admin'))
