import json

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .base import *
from polls.models import Wallet


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