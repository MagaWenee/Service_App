import falcon

MIDDLEWARE_TOKEN_KEY = "__SKIP_MIDDLEWARE_TOKEN__"

class Token:
    def __init__(self, key, value, pre=False):
        self.key = key
        self.value = value
        self.pre = pre

    async def process_request(self, req, resp):
        if not self.pre:
            return
        return self.__validate__(req)

    async def process_resource(self, req, resp, resource, params):
        """Validate Token"""
        skipper = getattr(resource, MIDDLEWARE_TOKEN_KEY, None)
        if skipper:
            return
        return self.__validate__(req)

    def __validate__(self, req):
        t = req.headers.get(self.key.lower(), False)

        if not t or t != self.value:
            # TODO: Change to Unautorized
            raise falcon.HTTPForbidden(
                title="Authentication Forbidden", description="Missing Token"
            )
        return