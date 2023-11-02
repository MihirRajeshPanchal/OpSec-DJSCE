from flask import Flask, request, jsonify
from passlib.hash import sha256_crypt

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    hashed_password = sha256_crypt.hash(password)

    users[username] = hashed_password

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in users:
        hashed_password = users[username]
        if sha256_crypt.verify(password, hashed_password):
            return jsonify({'message': 'Login successful'})
    
    return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run(debug=True)
