from flask import Flask, request, render_template
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            # Simulate subtle timing difference (optional)
            time.sleep(0.1)
            return render_template('dashboard.html')
        else:
            # No explicit failure message
            return render_template('error.html')
    except:
        return render_template('error.html')
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)