import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Request


class HelloAppTests(TestCase):
    fixtures = ['initial_data.json']

    def test_middleware_request(self):
        "middleware has to create Request object"

        self.assertEqual(len(Request.objects.all()), 0)
        self.client.get(reverse('hello:index'))
        requests = Request.objects.all()
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].status_code, 200)
        self.assertEqual(
            requests[0].request,
            'GET %s HTTP/1.1' % reverse('hello:index')
        )

    def test_ajax_handler(self):
        "test ajax handler"

        self.client.get(reverse('hello:index'))

        resp = self.client.get(
            reverse('hello:requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(resp.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]['fields']['request'],
            'GET %s HTTP/1.1' % reverse('hello:index'))
        self.assertEqual(data[0]['fields']['status_code'], 200)
