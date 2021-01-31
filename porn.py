from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Start():
    driver = webdriver.Firefox()
    driver.get("https://www.xvideos.com/")
    driver.set_window_size(1920, 1012)
    # elements = driver.find_elements_by_class_name("thumb")
    driver.find_element(By.LINK_TEXT, "Log in").click()
    # driver.find_element(By.CSS_SELECTOR, "#signin-form-block > fieldset").click()
    # driver.find_element(By.ID, "signin-form_login").click()
    driver.find_element(By.ID, "signin-form_password").send_keys("Facebookme1")
    driver.find_element(By.ID, "signin-form_login").send_keys("ngecu16@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".col-sm-offset-4 > .btn-danger:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".icf-cog:nth-child(2)").click()
    driver.find_element(By.ID, "mobile-login-btn").click()

    elems = driver.find_elements_by_css_selector(".thumb [href]")
    for el in elems:
        el.click()
        driver.find_element(By.CSS_SELECTOR, ".right > img:nth-child(2)").click()
        driver.execute_script("window.scrollTo(0,466)")
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        # actions.move_to_element(element, 0, 0).perform()
        driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > strong").click()


    # links = [elem.get_attribute('href') for elem in elems]
    # print(links)

Start()