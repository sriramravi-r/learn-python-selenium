import time

from selenium import webdriver

#options
#options=webdriver.ChromeOptions();
#below code will not close browser once execution completed
#options.add_experimental_option("detach",True)
#chrome driver service
#service=Service("path of the chrome driver")
#driver=webdriver.Chrome(service=service)

# webdriver driver service
driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)