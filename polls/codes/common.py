class Error:
    success = 0
    failed = 1


class Verify:
    required = "required"


#
class CodeStatus:
    success = 200
    param_error = 40001
    mobile_exist = 40002
    wallet_exist = 40003

    @classmethod
    def get_msg(cls, status):
        msg_map = {
            cls.success:      "成功",
            cls.param_error:  "参数错误",
            cls.mobile_exist: "手机号已存在",
            cls.wallet_exist: "钱包已存在"
        }
        return msg_map.get(status)