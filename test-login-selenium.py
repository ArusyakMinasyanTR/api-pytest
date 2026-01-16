import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_valid_login():
    # Set up the Chrome driver with Service
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # Click login
    driver.find_element(By.ID, "login-button").click()

    # Assert successful login by checking for presence of inventory page
    assert "inventory" in driver.current_url

    driver.quit()