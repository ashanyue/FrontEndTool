class BaseExceptionBox(Exception):
    message = 'Unknown Errors'
    status = -1


class CustomException(Exception):
    message = ''
    status = -2

    def __init__(self, message=None, status=None):
        if message:
            self.message = message

        if status:
            self.status = status


class NotLoggedIn(BaseException):
    message = 'Not Logged in'
    status = 4010
