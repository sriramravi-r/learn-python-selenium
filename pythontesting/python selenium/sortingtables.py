from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("headless")
option.add_argument("--ignore-certificate-errors") #this will ignore certification issue
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browsersortedvegiee=[]
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElements=driver.find_elements(By.CSS_SELECTOR,"td:nth-child(1)")
for ele in veggieWebElements:
    browsersortedvegiee.append(ele.text)
originalSortedList=browsersortedvegiee.copy()
browsersortedvegiee.sort()
assert browsersortedvegiee == originalSortedList