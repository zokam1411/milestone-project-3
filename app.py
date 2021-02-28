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
    categories = mongo.db.categories.find()
    ads = mongo.db.ads.find()
    return render_template('ads.html', ads=ads, categories=categories)


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
        flash('Registration successful! Please Log In using your details.')
        return redirect(url_for('login'))

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
                return redirect(url_for(
                    'profile', username=session['user']))
            else:
                # invalid password match
                flash('Incorrect Username or/and Password')
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash('Invalid Username or/and Password')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    username = mongo.db.users.find_one(
        {'username': session['user']}['username'])

    if session['user']:
        return render_template('profile.html', username=username)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('get_ads'))


@app.route('/add_ad', methods=['GET', 'POST'])
def add_ad():
    if request.method == 'POST':
        urgent = 'on' if request.form.get('urgent') else 'off'
        ad = {
            'category': request.form.get('category'),
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'photo': request.form.get('photo'),
            'price': request.form.get('price'),
            'payment': request.form.get('payment'),
            'location': request.form.get('location'),
            'phone': request.form.get('phone'),
            'urgent': urgent
        }
        mongo.db.ads.insert_one(ad)
        flash('Ad successfully added and is live now.')
        return redirect(url_for('get_ads'))
    categories = mongo.db.categories.find().sort('category', -1)
    return render_template('add_ad.html', categories=categories)


@app.route('/view_ad/<ad_id>')
def view_ad(ad_id):
    ad = mongo.db.ads.find_one({'_id': ObjectId(ad_id)})
    return render_template('view_ad.html', ad=ad)


@app.route('/view_category/<category_name>')
def view_category(category_name):
    category = mongo.db.categories.find_one({'category': category_name})
    ads = mongo.db.ads.find({'category': category_name})
    return render_template('view_category.html', category=category, ads=ads)


@app.route('/edit_ad/<ad_id>', methods=['GET', 'POST'])
def edit_ad(ad_id):
    ad = mongo.db.ads.find_one({'_id': ObjectId(ad_id)})
    categories = mongo.db.categories.find().sort('category', -1)
    return render_template('edit_ad.html', ad=ad, categories=categories)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
