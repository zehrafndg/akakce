# Generated by Selenium IDE
import pytest
from time import sleep
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

class TestCase():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_case(self):
    #kullanıcı bilgileri ile login olur
    self.driver.get(globalConstants.URL)
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a[2]")))
    self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a[2]").click()
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/form/span[1]/input")))
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/span[1]/input").click()
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/span[1]/input").send_keys("zehrafndgl049@gmail.com")
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/form/span[2]/input")))
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/span[2]/input").click()
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/span[2]/input").send_keys("1997Zehra")
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/form/input[3]")))
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/input[3]").click()
    sleep(1)
    assert "https://www.akakce.com/" == self.driver.current_url

    #arama yapar
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[3]/form/span/input")))
    self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/form/span/input").click()
    self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/form/span/input").send_keys("iphone")
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[3]/form/button")))
    self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/form/button").click()

    #ilk ürünü seçer ve ürüne gider
    self.driver.execute_script("window.scrollTo(0,100)")
    sleep(2)
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/ul/li[1]/a/span/span[5]/b")))
    self.driver.find_element(By.XPATH,"/html/body/div[2]/ul/li[1]/a/span/span[5]/b").click()

    #ürünü  takip listesine ekler
    self.driver.execute_script("window.scrollTo(0,500)")
    sleep(2)
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div/div[3]/div/div/span")))
    self.driver.find_element(By.XPATH,"/html/body/main/div[1]/div/div[3]/div/div/span").click()

    #ürün takip listesinde mi diye kontrol eder
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#H_f_v8")))
    self.driver.find_element(By.CSS_SELECTOR,"#H_f_v8").click()
    self.driver.execute_script("window.scrollTo(0,200)")
    sleep(3)
    assert "iphone" in self.driver.find_element(By.XPATH,"/html/body/div[2]").text.lower()

    
    
    
    










    
    
