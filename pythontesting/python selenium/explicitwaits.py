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
listofproducts=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
runtimeproductlist=[]
for r in result:
    #assignment2
    runtimeproductlist.append(r.find_element(By.XPATH,"./h4").text)
    r.find_element(By.XPATH,"./div/button").click() #locator chaining
assert listofproducts == runtimeproductlist
driver.find_element(By.CSS_SELECTOR,'.cart-icon img').click()
driver.find_element(By.XPATH,'//button[contains(text(),"PROCEED TO CHECKOUT")]').click()

#sum validation
totalAmount=0;
prices=driver.find_elements(By.CSS_SELECTOR,"td:nth-child(5) .amount")
for price in prices:
    totalAmount=int(price.text)+totalAmount
assert totalAmount == int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

driver.find_element(By.CLASS_NAME,'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,'promoBtn').click()
wait=WebDriverWait(driver,10)
# EXP_Wait target one element and wait until element location, Max_Limit upto 15 second
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'promoInfo')))
#assginment1
totamt=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
disamt=int(float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text))
assert totamt > disamt
driver.quit()