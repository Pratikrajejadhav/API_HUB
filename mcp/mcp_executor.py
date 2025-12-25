
from core.executor import Executor
from core.response import BaseResponse
import time

class MCPExecutor(Executor):
    def execute(self, request):
        time.sleep(1)
        return BaseResponse(200, {
            "action": request.payload.get("action"),
            "status": "executed"
        })
