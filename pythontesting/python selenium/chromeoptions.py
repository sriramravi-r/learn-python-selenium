from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
#option.add_argument("headless")
option.add_argument("--start-maximized")
option.add_argument("--ignore-certificate-errors") #this will ignore certification issue
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")