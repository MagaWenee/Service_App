
# Framework
import falcon
import falcon.asgi

# Middlewares
import middleware

# Endpoints
import endpoint

# Auth Token Init
token = middleware.Token("x-token", "abc123")

# Define App
app = falcon.asgi.App(middleware=[token])

# Router Definition
app.add_route('/', endpoint.DoS())

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0",port=8000, log_level="debug")