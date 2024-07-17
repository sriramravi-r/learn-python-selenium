from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name="sriram"

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert=driver.switch_to.alert
alert.accept()
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert=driver.switch_to.alert
alert.dismiss()
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)