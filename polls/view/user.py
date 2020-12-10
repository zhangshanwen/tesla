import json

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .base import *
from polls.models import User


@require_http_methods(["GET", "POST"])
def index(request):
    body = json.loads(request.body)
    print(body)
    return HttpResponse("get some thing ")


@require_http_methods(["POST"])
def login(request):
    param = {
        "mobile":   "required",
        "password": "required",
    }
    status = check_json_param(request, param)
    if not status:
        return Failed.params()
    return Success.success(json.loads(request.body))


@require_http_methods(["POST"])
def register(request):
    param = {
        "mobile":   "required",
        "password": "required",
    }
    status = check_json_param(request, param)
    if status:
        return Failed.params()
    user = User(**param)
    msg = user.create()
    if msg:
        return Failed.mobile_exist()
    return Success.success(param)
