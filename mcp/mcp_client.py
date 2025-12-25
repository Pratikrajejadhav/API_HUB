
from core.request import BaseRequest
from core.validator import Validator
from persistence.file_storage import FileStorage
from .mcp_executor import MCPExecutor
from datetime import datetime

class MCPClient:
    def __init__(self):
        self.exec = MCPExecutor()
        self.store = FileStorage()

    def send(self, action, parameters=None):
        req = BaseRequest("MCP_LOCAL","MCP",{
            "action":action,
            "parameters":parameters or {}
        })
        Validator.validate_request(req)
        resp = self.exec.execute(req)
        Validator.validate_response(resp)
        self.store.save({
            "type":"MCP",
            "timestamp":datetime.utcnow().isoformat(),
            "request":req.__dict__,
            "response":resp.__dict__
        })
        return resp
