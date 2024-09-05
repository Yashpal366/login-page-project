# test_login.py (Using Playwright in Python)
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser
        page = browser.new_page()  # Open a new page
        page.goto("http://localhost:3000")  # Navigate to the login page

        # Fill the login form
        page.fill("#username", "testuser")
        page.fill("#password", "testpassword")

        # Submit the form
        page.click("button[type='submit']")

        # Assert if login was successful by checking the page content
        assert "Login Successful!" in page.content()

        print("Login test passed!")
        browser.close()

if __name__ == "__main__":
    test_login()
