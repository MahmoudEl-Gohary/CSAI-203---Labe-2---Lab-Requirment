from .auth import authenticate_token
from .error_handling import register_error_handlers

def register_middleware(app):
    app.before_request(authenticate_token)  
    register_error_handlers(app)
