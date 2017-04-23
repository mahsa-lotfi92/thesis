import pickle

from django.core.handlers.wsgi import WSGIRequest

from ajax_testing.models import RequestEntry, MyWSGIRequest
from thesis.settings import SAVING_MODE

last_method = None

def save_request(function):
    global last_method

    def wrap(*args, **kwargs):
        global last_method

        if SAVING_MODE:

            my_args = []
            for a in args:
                if isinstance(a, WSGIRequest):
                    my_args.append(MyWSGIRequest(a))
                else:
                    my_args.append(a)

            input_args = pickle.dumps(tuple(my_args))

            entry = None

            try:
                output = function(*args, **kwargs)
                entry = RequestEntry(input_json=input_args, output_json=pickle.dumps(output),
                                     function_name=(function.__module__ + '.'+ function.__name__), success=True)
                entry.save()
                return output
            except Exception as e:
                entry = RequestEntry(input_json=input_args, function_name=(function.__module__ + '.' + function.__name__),
                                     success=False)
                entry.save()
                raise e
            finally:
                last_method = entry
        else:
            return function(*args, **kwargs)


    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap