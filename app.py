from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a real secret key

# Store messages (in a real app, you'd use a database)
messages = []

# Dummy users
users = {
    "AJ": "AJ123",
    "Chantelle": "Chantelle123"
}

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
    return render_template('chat.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials, please try again.'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/get_messages')
@login_required
def get_messages():
    # Retrieve all messages, user-specific styling will be handled on the frontend
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    message = request.json['message']
    username = session['username']
    
    # Determine message style and name based on the logged-in user
    if username == "AJ":
        color = "blue"
        side = "right"
        name = "AJ"
    elif username == "Chantelle":
        color = "#FA6583"
        side = "left"
        name = "Richantia"
    
    # Append the message with the user-specific info
    message_data = {
        "name": name,
        "message": message,
        "color": color,
        "side": side
    }
    messages.append(message_data)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)