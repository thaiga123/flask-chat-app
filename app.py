from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Store messages (in a real app, you'd use a database)
messages = []

# Simulating a simple user database
users = {
    'AJ': 'AJ123',
    'Chantell': 'Chantell123'
}

# A decorator to check if the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return render_template('chat.html', messages=messages, username=session['username'])

@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    message = request.form['message']
    username = session['username']
    
    # Add message with username to differentiate who sent it
    messages.append({'user': username, 'message': message})

    return jsonify({'status': 'success'}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are correct
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password', 403
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
