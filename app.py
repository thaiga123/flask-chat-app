from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

# Store messages (in a real app, you'd use a database)
messages = []

@app.route('/')
def home():
    # Check if user is logged in, if not, redirect to login
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate login credentials
        if (username == 'AJ' and password == 'AJ123') or (username == 'Chantell' and password == 'Chantell123'):
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))  # Redirect to chat page
        else:
            return "Invalid credentials", 403  # Simple error message for invalid login
    return render_template('login.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message_text = request.form['message']
    username = session.get('username')  # Get the username from the session
    messages.append({'text': message_text, 'sender': username})  # Store message with sender info
    return '', 200  # Return empty response, no need for a JSON message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
