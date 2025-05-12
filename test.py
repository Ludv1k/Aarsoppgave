import pymysql
import hashlib

def connect_db():
    return pymysql.connect(
        host="192.168.86.23",
        user="admin",
        password="strongpassword",
        database="testing",
        cursorclass=pymysql.cursors.DictCursor
    )

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# def do_stuff():
    
#     return(name, email, password)

def signup():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    db = connect_db()
    with db.cursor() as cursor:
        hashed_pw = hash_password(password)
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, hashed_pw))
        db.commit()
    db.close()
    print("Signup successful!")
    select()

def login(email, password):
    db = connect_db()
    with db.cursor() as cursor:
        hashed_pw = hash_password(password)
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sql, (email, hashed_pw))
        user = cursor.fetchone()
    db.close()

    if user:
        print("Login successful!")
        print(f"Welcome, {user['name']}!")
    else:
        print("Invalid email or password.")

def select():
    number = int(input("Chose between 1 [signup] or 2 [login]: "))
    if number == 1:
        signup()
    elif number == 2:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        login(email, password)
    else:
        print("invalid")
        select()



# do_stuff()
select()


# Example usage:
# signup("Alice", "alice@example.com", "secret123")
# login("alice@example.com", "secret123")
