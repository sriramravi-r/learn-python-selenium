import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options)
driver.implicitly_wait(5) #added implicit wait
# 5 second is max time out if element is display in 2 second it will save 3 seconds and run
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
#buttonlist=driver.find_elements(By.CSS_SELECTOR,".products div.product:nth-child(1) .product-action button")
#IMP_Wait will not work for findelements
result=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for r in result:
    r.find_element(By.XPATH,"./div/button").click() #locator chaining
driver.find_element(By.CSS_SELECTOR,'.cart-icon img').click()
driver.find_element(By.XPATH,'//button[contains(text(),"PROCEED TO CHECKOUT")]').click()
driver.find_element(By.CLASS_NAME,'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,'promoBtn').click()
wait=WebDriverWait(driver,10)
# EXP_Wait target one element and wait until element location, Max_Limit upto 15 second
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'promoInfo')))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)
driver.quit()