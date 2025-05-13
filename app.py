from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql #type: ignore
import hashlib
import re

# Create the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def connect_db():
    return pymysql.connect(
        # host="192.168.86.23",
        host="10.2.2.138",
        user="admin",
        password="strongpassword",
        database="testing",
        cursorclass=pymysql.cursors.DictCursor
    )

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Create route
@app.route('/')
def root():
    return render_template('base.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not is_valid_email(email):
            flash("Invalid email format"), 400

        hashed_pw = hash_password(password)

        db = connect_db()
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

        db = connect_db()
        with db.cursor() as cursor:
            sql = "SELECT name FROM users WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, hashed_pw))
            user = cursor.fetchone()
        db.close()

        if user:
            session['name'] = user['name']
            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for('root'))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Run the Flask app
if __name__ == '__main__':
    # Set the app to be accessible on the network
    app.run(host='0.0.0.0', port=8080, debug=True)