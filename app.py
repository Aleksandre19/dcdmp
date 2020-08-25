import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dcdmpDB'
app.config['MONGO_URI'] = 'mongodb+srv://dcdmpDBUser:PassWord@dcdmp.cs4wp.mongodb.net/dcdmpDB?retryWrites=true&w=majority'
app.secret_key = 'some secret kay'
mongo = PyMongo(app)

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



################ INSERTING IMAGE BOOK ###############

# Checking if file has a extension which is in allowed extensions list
def allowed_filesieze(filesize):

    if int(filesize) <= 0.5 * 1024 * 1024:
        return True
    else:
        return False    


# Checking if image has allowed extension
def allowed_ext(filename):
 
    ext = filename.rsplit('.',1)[1]
    allowed_ext = ['JPG', 'JPEG', 'PNG', 'gif']

    if ext.upper() in allowed_ext:
        return ext
    else:
        return False    


# Generating random filename
def generate_random_img_name():
    r_name = str(uuid.uuid4())
    return r_name


# Uploading image
def upload_image():

    image = request.files['file']
    # Checking image's settings
    if image.filename == '':
        flash('The image must have a name')
        redirect(request.url)
        return False

    if not allowed_filesieze(request.cookies.get('filesize')):
        flash("The allowed maximum image size is 500 KB ")
        redirect(request.url)
        return False

    if not allowed_ext(image.filename):
        flash("The allowed extensions are PNG, JPG, JPEG, GIF")  
        redirect(request.url)
        return False  
    # Saving image to folder
    img_folder_path = 'static/img/uploaded'
    r_f_name = generate_random_img_name() + '.' + allowed_ext(image.filename)
    image.save(os.path.join(img_folder_path, r_f_name))

    

# Insertting image
@app.route('/insert_book', methods=['POST'])
def insert_book():

    if request.method == "POST":
       
        upload_image()


    return redirect(url_for('add_book'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)