from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for sessions

# Store messages in memory (could use a database in a real app)
messages = []

# User credentials
users = {
    'AJ': 'AJ123',
    'Chantelle': 'Chantelle123'
}

@app.route('/')
def home():
    # Check if the user is logged in, if not, redirect to login
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate the username and password
        if username in users and users[username] == password:
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))  # Redirect to the chat page
        else:
            return 'Invalid credentials', 401  # Invalid login attempt

    return render_template('login.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    user = data['user']
    
    # Append message to the messages list
    messages.append({'content': message, 'user': user})
    
    # Send a response back with the message
    return jsonify({'message': message, 'user': user})

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from session
    return redirect(url_for('login'))  # Redirect to login page

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
