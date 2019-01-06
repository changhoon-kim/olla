from django.http import HttpResponse

import json

def hello(request):
    return HttpResponse(json.dumps({"code":200, "message":"OK"}))
