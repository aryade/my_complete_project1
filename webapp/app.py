from flask import Flask, render_template, request, redirect, url_for, flash

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

if __name__ == '__main__':
    app.run(debug=True)
