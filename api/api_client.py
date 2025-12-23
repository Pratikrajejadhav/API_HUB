
from core.request import BaseRequest
from core.validator import Validator
from persistence.file_storage import FileStorage
from .http_executor import HTTPExecutor
from datetime import datetime

class APIClient:
    def __init__(self):
        self.exec = HTTPExecutor()
        self.store = FileStorage()

    def send(self, endpoint, method, payload=None, headers=None):
        req = BaseRequest(endpoint, method, payload, headers)
        Validator.validate_request(req)
        resp = self.exec.execute(req)
        Validator.validate_response(resp)
        self.store.save({
            "type":"API",
            "timestamp":datetime.utcnow().isoformat(),
            "request":req.__dict__,
            "response":resp.__dict__
        })
        return resp
