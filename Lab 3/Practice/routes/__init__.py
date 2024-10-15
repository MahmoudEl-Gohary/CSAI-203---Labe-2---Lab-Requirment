from .book_store import book_store_bp

def register_routes(app):
    app.register_blueprint(book_store_bp, url_prefix='/books')
