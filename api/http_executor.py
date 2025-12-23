
import requests
from core.executor import Executor
from core.response import BaseResponse

class HTTPExecutor(Executor):
    def execute(self, request):
        try:
            r = requests.request(request.method, request.endpoint,
                                 json=request.payload, headers=request.headers, timeout=5)
            return BaseResponse(r.status_code, r.json() if r.content else None)
        except Exception as e:
            return BaseResponse(500, error=str(e))
