import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
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


################ My List ##################

# Check if user is in session
def check_session():
    if "user" in session and "email" in session:
        return True
    else:
        return False    


# Retrieving books from mongodb by users
def retriev_books_by_user(name,  email):
    book_id = mongo.db.users.find_one({'user_name' : name, 'user_email' : email})
    users_books = mongo.db.books.find({'_id' : {'$in' : book_id['added_books']}})
    return users_books



# My List
@app.route('/my_list')
def my_list():
    if check_session():
        return render_template('/my_list.html', books=retriev_books_by_user(session['user'], session['email']))

    return render_template("auth.html")
    

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/added_books')
def added_books():
    return render_template("added_books.html")


@app.route('/book_search')
def book_search():
    return  render_template("book_search.html")

# If the user already exists in mongo db so it will be saved onlly in session
# Otherwise it will be added as same as it will be saved in session also
def add_user_in_mongodb(name, email):
    # Adding user in mongodb if he/she is new
    if not mongo.db.users.find_one({'user_name' : name, 'user_email' : email}):
        mongo.db.users.insert_one({
            'user_name' : name ,
            'user_email' : email,
            'added_books' : []
        })

        session['user'] = name
        session['email'] = email

    # storing user in session
    session['user'] = name
    session['email'] = email   

    return True


################# Authentication ####################

# Log Out function
@app.route('/log_out')
def log_out():
    session.clear()
    return render_template('auth.html')


#Get books IDs
def get_books_id(name, email):
    user = mongo.db.users.find_one({'user_name' : name, 'user_email' : email})
    for u in user:
        book_id = int(u[added_books])
        return book_id


# Authentication page
@app.route('/auth', methods=['POST'])
def auth():

    # Checking if button was submited
    if request.method == 'POST':
        if not request.form['user_name'] and not request.form['user_email']:
            flash("In order to make authentication you must fill all fields")
            redirect(request.url)  

        # Making authentication 
        name = request.form['user_name'] 
        email = request.form['user_email']
        add_user_in_mongodb(name, email)

    # Rendering template and retrieving books by user      
    return render_template('my_list.html' , books = retriev_books_by_user(name, email))





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


f_name = ''

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
    global f_name 
    f_name = r_f_name
    return True



# Adding user in database
def adding_user(name, email, book_id):
    # If user is new then adding in database
    if not mongo.db.users.find_one({"user_name" : name, "user_email" : email}):
       mongo.db.users.insert_one({
           "user_name" : name,
           "user_email" : email,
           "added_books" : [book_id]
       })

    else:
       # If user already exists then updating added books list
       user = mongo.db.users.update_one({"user_name" : name, "user_email" : email}, {'$push': {"added_books" : book_id}})



# Insertting image
@app.route('/insert_book', methods=['POST'])
def insert_book():

    if request.method == "POST":
       
        if upload_image():
            
            book_id = ObjectId()
            
            # Adding user in database
            adding_user(request.form['user_name'], request.form['user_email'], book_id)

            # Adding books details in database
            mongo.db.books.insert_one({
                "_id" : book_id,
                'title' : request.form['title'],
                'author' : request.form['author'],
                'released_date' : request.form['released_date'],
                'language' : request.form['language'],
                'price' : request.form['price'],
                'description' : request.form['description'],
                'affiliante_link' : request.form['affiliante_link'],
                'image_name' : str(f_name),
                'searched' : 0,
                'my_list' : [],
                'book_of_day' : False,
                'special_offer' : False
            })

            flash("The book was add successfully ")    

    return redirect(url_for('add_book'))



############# Deleting books #############

@app.route('/delete_book')
def delete_book():

    # Avoiding a accessing straight from url
    if request.args.get('book_id') and request.args.get('img_name'):

        folder_path = 'static/img/uploaded'
        book_id = request.args.get('book_id')
        img_name = request.args.get('img_name')

        # Removing books from mongodb
        mongo.db.books.remove({'_id' : ObjectId(book_id)})

        # Deleting added book's ID from users collection
        mongo.db.users.update({'user_name' : session['user'], 'user_email' : session['email']}, {'$pull' : { 'added_books' : ObjectId(book_id) }})

        # Removing image from uploaded folder
        os.remove(os.path.join(folder_path, img_name))

        return redirect(url_for('my_list'))

    return redirect(url_for('my_list'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)