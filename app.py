from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for sessions

# Store messages (in a real app, you'd use a database)
messages = []

@app.route('/')
def home():
    # Check if the user is logged in, otherwise redirect to login
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials
        if (username == 'AJ' and password == 'AJ123') or (username == 'Chantell' and password == 'Chantell123'):
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))  # Redirect to the chat page
        else:
            return 'Invalid credentials', 401  # Return an error if login fails

    return render_template('login.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = json.loads(request.data)  # Get the JSON data
    message = data['message']
    user = data['user']
    
    # Append message to the message list
    messages.append({'content': message, 'user': user})
    
    # Send a JSON response back to the client
    return jsonify({'status': 'success', 'message': message, 'user': user}), 200

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))  # Redirect to login page after logout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
