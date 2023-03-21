from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class sauceDemoTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_bos_username_password(self):
        self.driver.find_element(By.ID,"login-button").click()
        error_message = self.driver.find_element(By.XPATH,"//h3").text
        if error_message == "Epic sadface: Username is required":
            print(error_message)
        sleep(3)    
    def test_bos_password(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"login-button").click()
        error_message = self.driver.find_element(By.XPATH,"//h3").text
        if error_message == "Epic sadface: Password is required":
            print(error_message)
        self.driver.find_element(By.ID,"user-name").clear()
        sleep(3)    
    def test_locked_out_user(self):
        self.driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        error_message = self.driver.find_element(By.XPATH,"//h3").text
        if error_message == "Epic sadface: Sorry, this user has been locked out.":
            print(error_message)
        self.driver.find_element(By.ID,"user-name").clear()
        self.driver.find_element(By.ID,"password").clear() 
        sleep(3)      
    def test_bos_inputs_x_icon(self):
        self.driver.find_element(By.ID,"login-button").click()
        error_icon = self.driver.find_elements(By.XPATH,"//form//div[@class='input-error form_group']")
        if len(error_icon) == 2:
            print(len(error_icon))
        close_button = self.driver.find_element(By.XPATH,"//button[@class='error-button']")
        close_button.click()
        sleep(1)
        self.driver.find_element(By.ID,"user-name").clear()
        self.driver.find_element(By.ID,"password").clear() 
        sleep(1)     
    def test_basarili_giris(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        sleep(1)
        self.driver.find_element(By.ID,"login-button").click()
        print(self.driver.current_url)
         

    def test_ürün_sayisi(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        ürün_sayisi = len(self.driver.find_elements(By.XPATH,"//div[@class='inventory_item']"))
        if ürün_sayisi == 6:
            print(ürün_sayisi)

test = sauceDemoTest()








