import json

from ajax_testing.models import RequestEntry
from thesis.settings import SAVING_MODE

last_method = None

def save_request(function):
    global last_method

    def wrap(*args, **kwargs):
        global last_method

        if SAVING_MODE:
            input_json = json.dumps(args)
            file = open('tests.txt', 'a')
            entry = None

            try:
                output = function(*args, **kwargs)
                entry = RequestEntry(input_json=input_json, output_json=json.dumps(str(output)),
                                     function_name=(function.__module__ + '.'+ function.__name__), success=True,
                                     previous_request=last_method)
                entry.save()
                file.write('{} {} \n'.format(input_json, json.dumps(str(output))))
                return output
            except Exception as e:
                entry = RequestEntry(input_json=input_json, function_name=(function.__module__ + '.' + function.__name__),
                                     success=False, previous_request=last_method)
                entry.save()
                file.write('{} \n'.format(input_json))
                raise e
            finally:
                last_method = entry
                file.close()
        else:
            return function(*args, **kwargs)


    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap