from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()  
    driver.get("https://myrealtordash.clareityiam.net/idp/login")

     # Find elements by name
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "loginbtn")
    # Enter credentials
    username_field.send_keys("1234567")
    password_field.send_keys("abcdefg")

    # Click login
    login_button.click()


    time.sleep(2)  # Wait for results to load

    assert "incorrect login ID or password" in driver.page_source
    driver.quit()


