from flask import Flask
from middleware import register_middleware
from routes import register_routes


app = Flask(__name__)

register_middleware(app)
register_routes(app)


if __name__ == "__main__":
    app.run(debug=True)
