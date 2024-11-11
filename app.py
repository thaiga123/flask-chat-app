from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Store messages (in a real app, you'd use a database)
messages = []

@app.route('/')
def home():
    return render_template('chat.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = json.loads(request.data)  # Get the JSON data
    message = data['message']
    user = data['user']
    
    # Append message to the message list
    messages.append({'content': message, 'user': user})
    
    # Send a JSON response back to the client
    return jsonify({'status': 'success', 'message': message, 'user': user}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
