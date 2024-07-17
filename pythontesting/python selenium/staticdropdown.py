from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

selectoptions=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
selectoptions.select_by_index(0)
selectoptions.select_by_visible_text("Female")
#selectoptions.select_by_value()