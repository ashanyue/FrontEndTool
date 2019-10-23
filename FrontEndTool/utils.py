from hashlib import md5
import re


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
    from . import settings
    '''取一个字符串的hash值'''
    # 提高字符串的复杂度
    pwd = '!@#$%' + pwd + '&^**('
    pwd = pwd + settings.PWD_SALT
    # 取str　hash值
    sh = md5()
    sh.update(pwd.encode('utf-8'))
    return sh.hexdigest()


class validator:
    def mobile(self, value):
        return re.match(r'^1\d{10}$', value) is not None

    def user_name(self, value):
        return re.match(r'^[\d,a-z,A-Z]+$', value) is not None
