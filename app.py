from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages (each message will include who sent it)
messages = []

@app.route('/')
def home():
    return render_template('chat.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    # Add sender info (here, assuming "me" is your messages and "her" is your girlfriend's)
    # You can replace these with actual logic, like checking who is logged in
    messages.append({'text': message, 'sender': 'me'})
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
