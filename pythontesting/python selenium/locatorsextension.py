from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"(//div[@class='card-text']/form/div/input)[1]").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@123")
driver.find_element(By.XPATH,"(//div[@class='card-text']/form/div/input)[3]").send_keys("Hello@123")
driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
