import pytest
from playwright.sync_api import sync_playwright

# Define the URL of your Flask app
BASE_URL = "http://127.0.0.1:5000"

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill('input#email', 'test@example.com')
        page.fill('input#password', 'password123')
        page.click('button[type="submit"]')
        assert "Welcome" in page.text_content('h1')
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill('input#email', 'sample@example.com')
        page.fill('input#password', '123456789')
        page.click('button[type="submit"]')
        assert "Invalid email or password" in page.text_content('.messages')
        browser.close()