import falcon
import httpx

class Do:
    __SKIP_MIDDLEWARE_TOKEN__ = False

    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.text = "OK"

class DoAudit:
    __SKIP_MIDDLEWARE_TOKEN__ = False

    async def on_post(self, req, resp):
        """Handles Post requests"""
        # Read Body
        # Log Info Body

        # Created Ok
        resp.status = falcon.HTTP_201


class DoApp:
    __SKIP_MIDDLEWARE_TOKEN__ = False

    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.text = "This is App"


class DoAuth:
    __SKIP_MIDDLEWARE_TOKEN__ = True

    async def on_get(self, req, resp):
        """Handles GET requests"""
        # Headers
        # JSON Body
      
        # If Basic != Vars 403
        user_from_someplace = "user"
        password_from_somplece = "pass"
      
        resp.status = falcon.HTTP_200
        resp.text = "This is App"


class DoS:
    __SKIP_MIDDLEWARE_TOKEN__ = True

    async def on_get(self, req, resp):
        """Handles GET requests"""
        # Basic Auth Method
        # If ok -> go else -> 403
        # Send Request to Audit App

        # Send request to Auth App
        r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
        if r.status_code != 200:
            raise falcon.HTTPForbidden(
                title="Authentication Forbidden", description="Invalid Credentials"
            )

        # Return response from App
        r = httpx.get('https://httpbin.org/get')

        if r.status_code != 200:
            raise falcon.HTTPUnautorized(
                title="Authentication Forbidden", description="Invalid Token"
            )
        resp.text =  r.text