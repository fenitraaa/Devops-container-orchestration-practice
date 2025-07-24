from flask import Flask, render_template, request, redirect
from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=3306,
        user=os.getenv('USER'),
        password=os.getenv('PASS'),
        database="flask_crud"
    )
    return connection

# Initialize database on first run
def init_db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=os.getenv('USER'),
        password=os.getenv('PASS')
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS flask_crud")
    cursor.execute("USE flask_crud")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

init_db()


@app.route("/")
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users ORDER BY id DESC")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', users=users)


@app.route("/adduser")
def adduserpage():
    return render_template("adduser.html")


@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        cursor.close()
        connection.close()
    return redirect("/")


@app.route("/delete/<int:id>")
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id =%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')


@app.route("/edit/<int:id>")
def edit_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    if user:
        return render_template("edituser.html", user=user)
    else:
        return redirect("/")


@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE users SET name=%s, email=%s WHERE id=%s",
            (name, email, id)
        )
        connection.commit()
        cursor.close()
        connection.close()
    return redirect('/')


@app.route("/date")
def date():
    d = datetime.now()
    return render_template('date.html', d=d)


@app.route("/sumpage")
def sumpage():
    return render_template('sum.html')


@app.route("/sum", methods=['POST'])
def sum_numbers():
    num1 = int(request.form.get('num1', 0))
    num2 = int(request.form.get('num2', 0))
    result = num1 + num2
    return render_template('sum.html', num1=num1, num2=num2, sum=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
