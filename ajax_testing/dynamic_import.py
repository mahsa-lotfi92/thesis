from importlib import import_module
import json
from ajax_testing.models import RequestEntry
from django.http.response import HttpResponse


def run_method(request):
    requests = RequestEntry.objects.filter()
    res = []
    for r in requests:
        name = r.function_name
        inputs= json.loads(r.input_json)
        p, m = name.rsplit('.', 1)
        module = import_module(p)
        try:
            method = getattr(module, m)
            if r.output_json == json.dumps(str(method(*inputs))):
                res.append('request entry ' + str(r.id) + ' was simulated successfully \n')
                r.success = True
                r.test_res = True
            else:
                res.append('Un equal result for request entry ' + str(r.id))
                r.test_res = False
        except Exception as e:
            r.success = False
            r.test_res = False
            res.append('failure at request entry ' + str(r.id) + e.__str__())
        finally:
            r.save()
    return HttpResponse(res)