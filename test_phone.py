# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPhone():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_phone(self):
    self.driver.get("https://www.phoneplacekenya.com/")
    self.driver.set_window_size(1920, 1012)
    self.driver.find_element(By.ID, "menu-all-departments-menu-1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#menu-all-departments-menu-1 > #menu-item-6295 > a").click()
    self.driver.find_element(By.CSS_SELECTOR, "#menu-all-departments-menu-1 > #menu-item-6301 > a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".departments-menu-v2-title > span").click()
    self.driver.find_element(By.CSS_SELECTOR, "#menu-all-departments-menu-2 > #menu-item-6295 > a").click()
  
