# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

def How():
    driver = webdriver.Firefox(options=options)
    driver.get("https://liveauction1.cash/login")
    driver.set_window_size(1920, 1012)
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "password").send_keys("Facebookme1@gmail.com")
    driver.find_element(By.ID, "email").send_keys("ngecu16@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".vlt-btn").click()

    time.sleep(0.5)

    driver.find_element(By.CSS_SELECTOR, ".kt-portlet:nth-child(1) .form-control").send_keys("1200")
    driver.find_element(By.CSS_SELECTOR, ".kt-portlet:nth-child(1) .btn").click()
    driver.find_element(By.CSS_SELECTOR, ".kt-widget17__items:nth-child(1) > .kt-widget17__item:nth-child(2) > .kt-widget17__desc").click()
    driver.implicitly_wait(10)
    print("Successfuly bid")

    driver.close()

How()