import pickle
from importlib import import_module

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from ajax_testing.models import RequestEntry
from django.http.response import HttpResponse


@csrf_exempt
def run_method(request):
    if settings.SAVING_MODE:
        return HttpResponse(None)

    start = request.POST.get('start')
    end = request.POST.get('end')

    if start and end:
        requests = RequestEntry.objects.filter(id__gte=start, id__lte=end)
    else:
        requests = RequestEntry.objects.all()

    res = []
    for r in requests:
        name = r.function_name
        input_args= pickle.loads(r.input_args)
        input_kwargs= pickle.loads(r.input_kwargs)
        p, m = name.rsplit('.', 1)
        module = import_module(p)
        try:
            method = getattr(module, m).as_view()
            response = method(*input_args, **input_kwargs).rendered_content

            if r.success and pickle.loads(r.output) == response:
                res.append('request entry ' + str(r.id) + ' was simulated successfully \n')
                r.success = True
                r.test_res = True
            else:
                res.append('Un equal result for request entry ' + str(r.id) + '\n')
                r.test_res = False

        except Exception as e:
            if not r.success:
                r.test_res = True
            elif r.success:
                r.test_res = False
            res.append('failure at request entry ' + str(r.id) + e.__str__() + '\n')
            # raise e

        finally:
            r.save()
    return HttpResponse(res)