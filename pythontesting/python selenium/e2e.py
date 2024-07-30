import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
#option.add_argument("headless")

driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,'//a[contains(text(),"Shop")]').click()
#by js executor we can open a new tab
#driver.execute_script("window.open('https://rahulshettyacademy.com/angularpractice/')")
#(//div[@class="card h-100"])[1]/child::div[@class="card-body"]/h4/a
#(//a/ancestor::h4)[1]
listofelements=driver.find_elements(By.XPATH, '//a/ancestor::h4')
for ele in listofelements:
    if ele.text == "iphone X":
        ele.find_element(By.XPATH,'.//following::button').click()
        break
driver.find_element(By.XPATH,"//a[contains(text(),'Checkout')]").click()
driver.find_element(By.XPATH,"(//tbody/tr//following::button)[3]").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="suggestions"]')))
suggestlist=driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul/li")
for ele in suggestlist:
    if ele.text == "India":
        ele.find_element(By.XPATH,"./a").click()
        break
driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.XPATH,'//form/input').click()
successmessage=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[contains(@class,"success")]'))).text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)" in successmessage
driver.close()