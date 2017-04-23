from django.core.handlers.wsgi import WSGIRequest
from django.db import models

# Create your models here.
class RequestEntry(models.Model):
    input_json = models.BinaryField()
    output_json = models.BinaryField()
    function_name = models.CharField(max_length=100)
    success = models.BooleanField()
    test_res = models.NullBooleanField(null=True)

    def __str__(self):
        return str(self.id)


class MyWSGIRequest(WSGIRequest):
    def __init__(self, wsgi):
        self.path = wsgi.path
        self.POST = wsgi.POST
        self.GET = wsgi.GET
        self.path_info = wsgi.path_info
        self.method = wsgi.method
        self.META = wsgi.META

        self.environ = wsgi.environ
        if 'wsgi.errors' in self.environ:
            del self.environ['wsgi.errors']
        if 'wsgi.input' in self.environ:
            del self.environ['wsgi.input']
        if 'wsgi.file_wrapper' in self.environ:
            del self.environ['wsgi.file_wrapper']

        # self.accepted_renderer = wsgi.accepted_renderer