from django.http import JsonResponse
from polls.codes.common import *
import json


class Success:
	@staticmethod
	def success(data, msg=None):
		code = CodeStatus.success
		return JsonResponse({
			"error": Error.success,
			"code":  code,
			"msg":   CodeStatus.get_msg(code) if not msg else msg,
			"data":  data
		})


class Failed:
	@classmethod
	def params(cls):
		return cls.failed(CodeStatus.param_error)

	@classmethod
	def mobile_exist(cls):
		return cls.failed(CodeStatus.mobile_exist)

	@staticmethod
	def failed(code: int, msg=None):
		return JsonResponse({
			"error": Error.failed,
			"code":  code,
			"msg":   CodeStatus.get_msg(code) if not msg else msg,
			"data":  ""
		})


def check_json_param(request, param: dict) -> Error.failed:
	if not request.body:
		return
	try:
		body = json.loads(request.body)
		for k, v in param.items():
			if v == Verify.required and not body.get(k):
				return
			param[k] = body.get(k)
		return Error.success
	except TypeError as e:
		print(e)
		return