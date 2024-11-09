from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages (in a real app, you'd use a database)
messages = []

@app.route('/')
def home():
    return render_template('chat.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
