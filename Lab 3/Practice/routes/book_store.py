from flask import Blueprint, jsonify, request

book_store_bp = Blueprint('book_store', __name__)

books = [
    {"id": 1, "title": "book1", "author": "author1", "price": 10.99},
    {"id": 2, "title": "book2", "author": "author2", "price": 12.99}
]

@book_store_bp.route('/', methods=['GET'])
def get_books():
    return jsonify(books), 200

@book_store_bp.route('/', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify({"message": "Book added", "book": new_book}), 201

@book_store_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(updated_data)
            return jsonify({"message": "Book updated", "book": book}), 200
    return jsonify({"error": "Book not found"}), 404

@book_store_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200