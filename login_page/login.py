# Sample user database
user_db = {
    "admin": "admin123",
    "user1": "password1",
    "testuser": "testpass"
}

def login_system(username, password):
    if username in user_db and user_db[username] == password:
        return "Login successful!"
    else:
        return "Invalid username or password!"

