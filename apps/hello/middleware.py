from apps.hello.models import Request


class LogRequestMiddleware(object):
    " Log HTTP Requests to database "

    def process_response(self, request, response):
        if not request.is_ajax():
            Request.objects.create(
                remote_addr=request.META['REMOTE_ADDR'],
                request="%s %s %s" % (
                    request.META['REQUEST_METHOD'],
                    request.META['PATH_INFO'],
                    request.META['SERVER_PROTOCOL']),
                status_code=response.status_code)
        return response
