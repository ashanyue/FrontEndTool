from hashlib import md5
from functools import wraps
from django.http import JsonResponse
from django.conf import settings
import logging, re


def json_response_format(data=None, status=200, message=None):
    """
    json数据返回格式化
    :return:
    """
    result = {"status": status}
    if message:
        result['message'] = message
    if data:
        result['data'] = data
    return result


def pwd_md5(pwd):
    '''取一个字符串的hash值'''
    # 提高字符串的复杂度
    pwd = '!@#$%' + pwd + '&^**('
    pwd = pwd + settings.PWD_SALT
    # 取str　hash值
    sh = md5()
    sh.update(pwd.encode('utf-8'))
    return sh.hexdigest()


class validator:
    @staticmethod
    def mobile(value):
        try:
            return re.match(r'^1\d{10}$', value)
        except:
            return None

    @staticmethod
    def user_name(value):
        try:
            return re.match(r'^[\d,a-z,A-Z]+$', value)
        except Exception:
            return None


def JsonRep(errors=None):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            try:
                result = func(request, *args, **kwargs)
                logging.debug(result)
                logging.debug(type(result))
                logging.debug(isinstance(result, dict))
                return JsonResponse(json_response_format(data=result, status=200))
            except Exception as err:
                if len(err.args):
                    err = list(err.args)[0]
                    if type(err) is str:
                        try:
                            error_code = int(err)
                        except:
                            error_code = 0
                    elif type(err) is int:
                        error_code = err
                    else:
                        error_code = 0
                    logging.debug(error_code)
                    if errors and str(error_code) in errors.keys():
                        error_msg = errors[str(error_code)]
                    else:
                        error_msg = "未知错误"
                else:
                    error_code = 0
                    error_msg = "未知错误"

                return JsonResponse(json_response_format(message=error_msg, status=error_code),
                                    json_dumps_params={'ensure_ascii': False}, charset='utf-8')

        return returned_wrapper

    return decorator
