
class BaseRequest:
    def __init__(self, endpoint, method, payload=None, headers=None):
        self.endpoint = endpoint
        self.method = method
        self.payload = payload
        self.headers = headers or {}
