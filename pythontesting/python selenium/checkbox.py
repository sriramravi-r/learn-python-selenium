from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.find_element(By.CSS_SELECTOR, "input[name='checkBoxOption2']").is_selected())
driver.find_element(By.CSS_SELECTOR, "input[name='checkBoxOption2']").click()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()