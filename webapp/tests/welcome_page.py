import pytest
from playwright.sync_api import sync_playwright

# Define the URL of your Flask app
BASE_URL = "http://127.0.0.1:5000"

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill('input#email', 'test@example.com')
        page.fill('input#password', 'password123')
        page.click('button[type="submit"]')
        page.get_by_role('Welcome')
        page.get_by_role("link", name="Back to Login").click()
        browser.close()