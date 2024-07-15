from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
#Locators - ID, NAME, XPATH , CSS_SELECTOR, LINKTEXT
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("sri@yopmail.com")
driver.find_element(By.XPATH,"//input[contains(@id,'exampleInputPassword')]").send_keys("123456")
driver.find_element(By.XPATH,"//input[contains(@id,'exampleCheck')]").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").is_displayed()
message=driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").text
assert "Success" in message
driver.find_element(By.XPATH,"//form-comp/child::div/child::h4/input").send_keys("hello")
driver.find_element(By.XPATH,"//form-comp/child::div/child::h4/input").clear()