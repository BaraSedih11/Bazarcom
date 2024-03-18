from datetime import datetime
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
import os
from marshmallow import Schema, fields
from werkzeug.security import generate_password_hash
# from flask_migrate import Migrate
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
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
    author = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    category = db.Column(db.String)


    def __init__(self, title, author, price, quantity, category=None):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', price={self.price}, quantity={self.quantity}, category='{self.category}')>"



# Schemas
class BookSchema(ma.Schema):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'quantity', 'category')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

with app.app_context():
    # db.drop_all()
    db.create_all()
    # book1 = Book(title='Book 1', author='Author 1', price=10.99, quantity=100)
    # book2 = Book(title='Book 2', author='Author 2', price=15.99, quantity=50)
    # db.session.add(book1)
    # db.session.add(book2)
    # db.session.commit()


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)

    return jsonify(result), 200



if __name__ == '__main__':
    app.run(debug=True)

    
