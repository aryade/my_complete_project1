import pytest
from playwright.sync_api import sync_playwright
import json

BASE_URL = "http://127.0.0.1:5000"

def test_api_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        # Use json.dumps to convert dictionary to JSON string
        response = context.request.post(
            f"{BASE_URL}/api/login",
            data=json.dumps({
                "email": "test@example.com",
                "password": "password123"
            }),
            headers={"Content-Type": "application/json"}
        )
        assert response.status == 200
        json_response = response.json()
        assert json_response["status"] == "success"
        assert json_response["message"] == "Login successful"

        browser.close()

def test_api_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Use json.dumps to convert dictionary to JSON string
        response = context.request.post(
            f"{BASE_URL}/api/login",
            data=json.dumps({
                "email": "invalid@example.com",
                "password": "wrongpassword"
            }),
            headers={"Content-Type": "application/json"}
        )


        assert response.status == 401
        json_response = response.json()
        assert json_response["status"] == "failure"
        assert json_response["message"] == "Invalid email or password"

        browser.close()
