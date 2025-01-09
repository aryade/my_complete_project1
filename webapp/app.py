from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'secret-key'  # For session and flash messages

# Dummy user data for testing
USER_DATA = {
    "test@example.com": "password123"
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email in USER_DATA and USER_DATA[email] == password:
        return redirect(url_for('welcome'))
    else:
        flash('Invalid email or password', 'error')
        return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    # if not data:
    #     return jsonify({"message": "Missing data"}), 400  # Get JSON data from the request
    email = data.get('email')
    password = data.get('password')

    # Check if the credentials are valid
    if email in USER_DATA and USER_DATA[email] == password:
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid email or password", "status": "failure"}), 401

if __name__ == '__main__':
    app.run(debug=True)
