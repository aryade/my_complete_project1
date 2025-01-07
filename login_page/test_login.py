import unittest
from login import login_system

class TestLoginSystem(unittest.TestCase):
    def test_valid_login(self):
        self.assertEqual(login_system("admin", "admin123"), "Login successful!")

    def test_invalid_username(self):
        self.assertEqual(login_system("invalid_user", "admin123"), "Invalid username or password!")

    def test_invalid_password(self):
        self.assertEqual(login_system("admin", "wrongpass"), "Invalid username or password!")

    def test_empty_username(self):
        self.assertEqual(login_system("", "admin123"), "Invalid username or password!")

    def test_empty_password(self):
        self.assertEqual(login_system("admin", ""), "Invalid username or password!")

    def test_case_sensitivity(self):
        self.assertEqual(login_system("Admin", "admin123"), "Invalid username or password!")

if __name__ == "__main__":
    unittest.main()