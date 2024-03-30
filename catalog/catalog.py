from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'catalog_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
# migrate = Migrate(app, db)
app.secret_key = '12345678'


# Models
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    topic = db.Column(db.String)


    def __init__(self, title, price, quantity, topic=None):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.topic = topic

    def __repr__(self):
        return f"<Book(title='{self.title}', price={self.price}, quantity={self.quantity}, topic='{self.topic}')>"


class BookSchema(ma.Schema):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'quantity', 'topic')

book_schema = BookSchema()
books_schema = BookSchema(many=True)


# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     book1 = Book(title='How to get a good grade in DOS in 40 minutes a day', topic="distributed_systems", price=10.99, quantity=100)
#     book2 = Book(title='RPCs for Noobs', topic="distributed_systems", price=15.00, quantity=50)
#     book3 = Book(title='Xen and the Art of Surviving Undergraduate School', topic="undergraduate_school", price=5.00, quantity=30)
#     book4 = Book(title='Cooking for the Impatient Undergrad', topic="undergraduate_school", price=10.00, quantity=70)
#     db.session.add(book1)
#     db.session.add(book2)
#     db.session.add(book3)
#     db.session.add(book4)
#     db.session.commit()

@app.route('/catalog/', methods=['GET'])
def get_bookss():
    
    return jsonify({"message" : "hello world"}), 200
    


@app.route('/catalog/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result), 200
    

@app.route('/catalog/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = Book.query.get_or_404(book_id)
    # Serialize the book object into a dictionary
    serialized_book = book_schema.dump(book)
    return jsonify(serialized_book)


@app.route('/catalog/books/<string:topic>', methods=['GET'])
def get_book_by_topic(topic):
    books = Book.query.filter_by(topic=topic).all()
    
    # Check if any books were found for the given topic
    if not books:
        return jsonify({'message': 'No books found for the specified topic'}), 404
    
    # Serialize the list of book objects into a list of dictionaries
    serialized_books = [book_schema.dump(book) for book in books]
    
    # Return the serialized list of book objects as JSON
    return jsonify(serialized_books)



@app.route('/catalog/books/<int:book_id>/decreament', methods=['POST'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    # Serialize the book object into a dictionary
    if book.quantity > 0:
        book.quantity -= 1
    else:
        return jsonify({"message": "Book not found"}), 404

    db.session.commit()
    # serialized_book = book_schema.dump(book)
    return jsonify({"message": "Book decreamented successfully", "book_id": book.id, "total_price": book.price})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


