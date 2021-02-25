import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (generate_password_hash,
                               check_password_hash, safe_str_cmp)
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_ads')
def get_ads():
    ads = mongo.db.ads.find()
    return render_template('ads.html', ads=ads)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': username})
        # check if passwords are same
        password_confirm = safe_str_cmp(password, confirm)

        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        elif not password_confirm:
            flash('Passwords do not match, please try again')
            return redirect(url_for('register'))

        register = {
            'username': username,
            'password': generate_password_hash(password)
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session['user'] = username
        flash('Registration successful!')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': username})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user['password'], password):
                session['user'] = username
                flash('Welcome {}'.format(username))
            else:
                # invalid password match
                flash('Incorrect Username or/and Password')
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash('Invalid Username or/and Password')
            return redirect(url_for('login'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
