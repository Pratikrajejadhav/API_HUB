
class Validator:
    @staticmethod
    def validate_request(req):
        if not req.endpoint or not req.method:
            raise ValueError("Invalid request")

    @staticmethod
    def validate_response(resp):
        if resp.status is None:
            raise ValueError("Invalid response")
