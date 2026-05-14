from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# Sample user data
USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.route('/')
def home():
    """Home endpoint"""
    return "Welcome to Flask Load Testing Demo!"

@app.route('/api/users')
def get_all_users():
    """Get all users"""
    return jsonify(USERS)

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    """Get specific user by ID"""
    user = next((u for u in USERS if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/search')
def search():
    """Search endpoint"""
    return jsonify({"results": [USERS[0], USERS[1]]})

@app.route('/api/slow')
def slow_endpoint():
    """Intentionally slow endpoint for testing"""
    time.sleep(random.uniform(1, 3))
    return jsonify({"status": "slow response completed"})

@app.route('/irctc')
def irctc():
    """Health check endpoint"""
    return jsonify({"status": "checked"})

@app.route('/media')
def media():
    """media check endpoint"""
    return jsonify({"status": "capptured"})

if __name__ == '__main__':
    app.run(debug=True, port=5005)