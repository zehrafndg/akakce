import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants
from webdriver_manager.chrome import ChromeDriverManager 

class HappyPath():
    def setup_method(self,method):
        self.driver = webdriver.Chrome(ChromeDriverManager.install())
        self.vars = {}
    
    def test_login(self):
        self.driver.get(globalConstants.URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"ul.nav-right > li:nth-child(2) > a" ))
        self.driver.find_element(By.CSS_SELECTOR,"ul.nav-right > li:nth-child(2) > a").click()


    def teardown_method(self,method):
        self.driver.quit()

