import os
import gridfs
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (generate_password_hash,
                               check_password_hash, safe_str_cmp)
from datetime import datetime
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


# display categories and 8 recently added ads on main page
@app.route('/')
@app.route('/get_ads')
def get_ads():
    categories = mongo.db.categories.find().sort('category', 1)
    ads = mongo.db.ads.find().sort('_id', -1).limit(8)
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'ads.html', ads=ads, categories=categories, admin=admin)

    return render_template('ads.html', ads=ads, categories=categories)


# register new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for("get_ads"))

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
            flash('Username already exists', 'blue lighten-1')
            return redirect(url_for('register'))

        elif not password_confirm:
            flash('Passwords do not match, please try again', 'red')
            return redirect(url_for('register'))

        register = {
            'username': username,
            'password': generate_password_hash(password),
            'join_date': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
            'status': 'normal'
        }
        mongo.db.users.insert_one(register)
        flash('Registration successful! Please Log in now', 'green')
        return redirect(url_for('login'))

    return render_template('register.html')


# login user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        redirect(url_for('get_ads'))

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': username})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user['password'], password):
                # put new user into session cookie
                session['user'] = username
                # update user login date
                mongo.db.users.update_one(
                    {'username': session['user']},
                    {'$set': {'last_log':
                              datetime.now().strftime('%d-%m-%y %H:%M:%S')}})

                return redirect(url_for(
                    'profile', username=session['user']))

            else:
                # invalid password match
                flash('Invalid Username or/and Password', 'red')
                return redirect(url_for('login'))

        else:
            # username doesn't exist
            flash('Invalid Username or/and Password', 'red')
            return redirect(url_for('login'))

    return render_template('login.html')


# user profile page
@app.route('/profile/<username>')
def profile(username):
    username = mongo.db.users.find_one(
        {'username': username})
    ads = mongo.db.ads.find({'created_by': username['username']})

    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'profile.html', username=username,
            ads=ads, admin=admin)

    return render_template('profile.html', username=username, ads=ads)


# add ad
@app.route('/add_ad', methods=['GET', 'POST'])
def add_ad():
    if 'user' not in session:
        flash('To place ad log in first', 'blue lighten-1')
        return redirect(url_for('login'))

    if request.method == 'POST':
        urgent = 'on' if request.form.get('urgent') else 'off'
        paypal = 'yes' if request.form.get('paypal') else 'no'
        cash = 'yes' if request.form.get('cash') else 'no'
        bitcoin = 'yes' if request.form.get('bitcoin') else 'no'
        result = None

        # add image to database
        if 'item_image' in request.files:
            item_image = request.files['item_image']
            if item_image.filename != '':
                result = mongo.save_file(item_image.filename, item_image)

        ad = {
            'category': request.form.get('category'),
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'item_image': item_image.filename,
            'price': request.form.get('price'),
            'location': request.form.get('location'),
            'phone': request.form.get('phone'),
            'urgent': urgent,
            'paypal': paypal,
            'bitcoin': bitcoin,
            'cash': cash,
            'created_by': session['user'],
            'date': datetime.now().strftime("%d/%m/%Y"),
            'img_id': result
        }

        mongo.db.ads.insert_one(ad)
        flash('Ad successfully added and is live now', 'green')
        return redirect(url_for('get_ads'))

    counties = mongo.db.counties.find().sort('county', 1)
    categories = mongo.db.categories.find().sort('category', 1)

    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'add_ad.html', categories=categories,
            counties=counties, admin=admin)

    return render_template(
        'add_ad.html', categories=categories, counties=counties)


# retrieve images from mongoDB
@app.route('/img_uploads/<filename>')
def img_uploads(filename):
    return mongo.send_file(filename)


# view add
@app.route('/view_ad/<ad_id>')
def view_ad(ad_id):
    # increment the number of views everytime a recipe is seen
    mongo.db.ads.update_one(
        {"_id": ObjectId(ad_id)}, {'$inc': {'views': 1}})

    ad = mongo.db.ads.find_one({'_id': ObjectId(ad_id)})
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        mod = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'mod'})

        if admin:
            return render_template(
                'view_ad.html', ad=ad, admin=admin)
        elif mod:
            return render_template(
                'view_ad.html', ad=ad, mod=mod)

    return render_template('view_ad.html', ad=ad)


# edit ad
@app.route('/edit_ad/<ad_id>', methods=['GET', 'POST'])
def edit_ad(ad_id):

    if request.method == 'POST':
        urgent = 'on' if request.form.get('urgent') else 'off'
        paypal = 'yes' if request.form.get('paypal') else 'no'
        cash = 'yes' if request.form.get('cash') else 'no'
        bitcoin = 'yes' if request.form.get('bitcoin') else 'no'
        result = None

        # check if new image selected
        if 'item_image' in request.files:
            item_image = request.files['item_image']
            if item_image.filename == '':
                item_image.filename = request.form.get('item_image_up')
            else:
                # if new image selected delete old from mongoDB
                ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
                img_id = ad["img_id"]
                if img_id:
                    files_id = mongo.db.fs.files.find_one(
                        {"_id": img_id})["_id"]
                    mongo.db.fs.chunks.remove({"files_id": ObjectId(files_id)})
                    mongo.db.fs.files.remove({"_id": ObjectId(img_id)})

                result = mongo.save_file(item_image.filename, item_image)

        update = {
            'category': request.form.get('category'),
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'item_image': item_image.filename,
            'price': request.form.get('price'),
            'location': request.form.get('location'),
            'phone': request.form.get('phone'),
            'urgent': urgent,
            'paypal': paypal,
            'bitcoin': bitcoin,
            'cash': cash,
            'created_by': request.form.get('created_by'),
            'updated': datetime.now().strftime("%d/%m/%Y"),
            'views': int(request.form.get('views')),
            'date': request.form.get('date'),
            'img_id': result
        }

        mongo.db.ads.update({'_id': ObjectId(ad_id)}, update)
        flash('Ad successfully updated', 'green')
        return redirect(url_for('view_ad', ad_id=ad_id))

    ad = mongo.db.ads.find_one({'_id': ObjectId(ad_id)})
    categories = mongo.db.categories.find().sort('category', -1)
    counties = mongo.db.counties.find().sort('category', -1)

    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        mod = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'mod'})
        advertiser = mongo.db.ads.find_one(
            {'_id': ObjectId(ad_id), 'created_by': session['user']})

        if admin:
            return render_template('edit_ad.html',
                                   ad=ad, categories=categories,
                                   counties=counties, admin=admin)
        elif mod:
            return render_template('edit_ad.html',
                                   ad=ad, categories=categories,
                                   counties=counties, mod=mod)
        elif advertiser:
            return render_template('edit_ad.html',
                                   ad=ad, categories=categories,
                                   counties=counties, advertiser=advertiser)

    return redirect(url_for('get_ads'))


@app.route('/all_ads')
def all_ads():
    ads = mongo.db.ads.find()
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'all_ads.html', ads=ads,  admin=admin)
    return render_template('all_ads.html', ads=ads)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    ads = mongo.db.ads.find({'$text': {'$search': query}})
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'search.html', ads=ads, admin=admin)
    return render_template('search.html', ads=ads)


@app.route('/logout')
def logout():
    flash('You have been logged out', 'blue lighten-1')
    session.pop('user')
    return redirect(url_for('get_ads'))


@app.route('/view_category/<category_name>')
def view_category(category_name):
    category = mongo.db.categories.find_one({'category': category_name})
    ads = mongo.db.ads.find({'category': category_name})

    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'view_category.html', category=category, ads=ads, admin=admin)

    return render_template('view_category.html', category=category, ads=ads)


@app.route('/search_cat/<category_name>', methods=['GET', 'POST'])
def search_cat(category_name):
    query = request.form.get('query')
    ads = mongo.db.ads.find({'$text': {'$search': query},
                             'category': category_name})
    category = mongo.db.categories.find_one({'category': category_name})
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        return render_template(
            'search_cat.html', ads=ads, category=category, admin=admin)
    return render_template('search_cat.html', category=category, ads=ads)


@app.route('/delete_ad/<ad_id>')
def delete_ad(ad_id):
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        mod = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'mod'})
        advertiser = mongo.db.ads.find_one(
            {'_id': ObjectId(ad_id), 'created_by': session['user']})

        if admin or mod or advertiser:

            ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
            img_id = ad["img_id"]

            if img_id:
                files_id = mongo.db.fs.files.find_one(
                    {"_id": img_id})["_id"]
                mongo.db.fs.chunks.remove({"files_id": ObjectId(files_id)})
                mongo.db.fs.files.remove({"_id": ObjectId(img_id)})

            mongo.db.ads.remove({"_id": ObjectId(ad_id)})
            flash('Ad successfully deleted', 'green')
            return redirect(url_for('get_ads'))
    return redirect(url_for('get_ads'))


@app.route('/report_ad/<ad_id>', methods=['GET', 'POST'])
def report_ad(ad_id):
    if 'user' not in session:
        return redirect(url_for('view_ad', ad_id=ad_id))

    if request.method == 'POST':
        mongo.db.ads.update_one(
            {"_id": ObjectId(ad_id)},
            {'$push': {'reports': request.form.get('report')}})
    flash('Ad reported, thank you.', 'green')
    return redirect(url_for('view_ad', ad_id=ad_id))


@app.route('/delete_report/<ad_id>')
def delete_report(ad_id):
    if 'user' in session:
        admin = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'admin'})
        mod = mongo.db.users.find_one(
            {'username': session['user'], 'status': 'mod'})

        if admin or mod:
            mongo.db.ads.update(
                {'_id': ObjectId(ad_id)}, {'$unset': {'reports': ""}})
            flash('Reports successfully deleted', 'green')
            return redirect(url_for('view_ad', ad_id=ad_id))

    return redirect(url_for('view_ad', ad_id=ad_id))


# admin control panel
@app.route('/control_panel')
def control_panel():
    categories = mongo.db.categories.find()
    users = mongo.db.users.find()
    ads = mongo.db.ads.find()

    return render_template('control_panel.html',
                           categories=categories, users=users, ads=ads)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        icon = request.form.get('icon')
        # check if category already exists in db
        existing_category = mongo.db.categories.find_one(
            {'category': category_name})
        # check if icon already exists in db
        existing_icon = mongo.db.categories.find_one(
            {'icon': icon})

        if existing_category:
            flash('Category already exists', 'blue lighten-1')
            return redirect(url_for('add_category'))

        elif existing_icon:
            flash('Icon already exists', 'blue lighten-1')
            return redirect(url_for('add_category'))

        cat = {
            'category': request.form.get('category_name'),
            'icon': request.form.get('icon')
        }
        mongo.db.categories.insert_one(cat)
        flash('Category successfully added', 'green')
        return redirect(url_for('control_panel'))
    return render_template('add_category.html')


@app.route('/edit_category/<category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    if request.method == 'POST':
        update = {
            'category': request.form.get('category_name'),
            'icon': request.form.get('icon')
        }
        mongo.db.categories.update({'_id': ObjectId(category_id)}, update)
        flash('Category successfully updated', 'green')
        return redirect(url_for('control_panel'))
    category = mongo.db.categories.find_one({'_id': ObjectId(category_id)})
    return render_template('edit_category.html', category=category)


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    flash('Category successfully deleted', 'green')
    return redirect(url_for('control_panel'))


@app.route('/delete_user/<username>')
def delete_user(username):
    # check if user have ads
    check_ads = mongo.db.ads.find_one({'created_by': username})
    if check_ads:
        mongo.db.ads.remove({'created_by': username})
    mongo.db.users.remove({'username': username})
    flash('User successfully deleted', 'green')
    return redirect(url_for('control_panel'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
