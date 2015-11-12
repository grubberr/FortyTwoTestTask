import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Request


class LogRequestMiddlewareTests(TestCase):
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

    def test_plain_http_request(self):
        """
        non-ajax http request to 'requests' has to return html code page
        """

        response = self.client.get(reverse('hello:requests'))
        self.assertTrue(response['content-type'].startswith('text/html'))
        self.assertContains(response, 'DOCTYPE html', 1)

    def test_ajax_http_request(self):
        """
        ajax http request to 'requests' has to return json object
        """

        response = self.client.get(
            reverse('hello:requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(response['content-type'], 'application/json')
        self.assertTrue(response.content, '[]')

    def test_ajax_handler(self):
        """
        created one Request object has to be accessible via ajax handler
        """

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

    def test_10_object(self):
        """
        make sure ajax handler return only last 10 Request objects
        """

        for i in xrange(20):
            self.client.get("/%d/non-existent-url/%d" % (i, i))

        records = list(Request.objects.order_by('-date_time')[:10])

        resp = self.client.get(
            reverse('hello:requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(resp.content)

        self.assertEqual(len(data), 10)

        for i in xrange(10):
            self.assertEqual(data[i]['fields']['request'], records[i].request)
