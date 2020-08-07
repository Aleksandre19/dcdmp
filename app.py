import os
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/add_book')
def add_book():
    return render_template("add_book.html")


@app.route('/my_list')
def my_list():
    return render_template("my_list.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/added_books')
def added_books():
    return render_template("added_books.html")


@app.route('/book_search')
def book_search():
    return  render_template("book_search.html")


@app.route('/auth')
def auth():
    return render_template("auth.html")


@app.route('/single_book_page')
def single_book_page():
    return render_template("single_book_page.html")    





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)