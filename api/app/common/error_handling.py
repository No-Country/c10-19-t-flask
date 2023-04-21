class AppErrorBaseClass(Exception):
   pass
class ObjectNotFound(AppErrorBaseClass):
   pass
class AuthError(AppErrorBaseClass):
   pass

from flask import jsonify, request

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['msg'] = self.message
        return rv
