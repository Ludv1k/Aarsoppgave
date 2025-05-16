from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql #type: ignore
import hashlib
import re
from config import db_config

# Create the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'


conn = pymysql.connect(**db_config)
cursor = conn.cursor(dictionary=True)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Create route
@app.route('/')
def root():
    name = session.get('name')
    return render_template('index.html', name=name)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not is_valid_email(email):
            flash("Invalid email format"), 400

        hashed_pw = hash_password(password)

        db = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, hashed_pw))
            db.commit()
        db.close()

        return redirect(url_for('root')) #redirect after signing up
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_pw = hash_password(password)

        db = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT name FROM users WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, hashed_pw))
            user = cursor.fetchone()
        db.close()
        
        if user:
            session['name'] = user['name']
            flash("Login successful!", "success")
            return redirect(url_for('root'))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('root'))

@app.route('/products')
def products():
    try:
        conn = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        product_list = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error fetching products: {e}")
        product_list = []

    return render_template('products.html', products=product_list)

# Run the Flask app
if __name__ == '__main__':
    # Set the app to be accessible on the network
    app.run(host='0.0.0.0', port=8080, debug=True)