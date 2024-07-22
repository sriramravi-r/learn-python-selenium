import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
parent_window=driver.current_window_handle
email=""
driver.find_element(By.XPATH,"//a[contains(text(),'Free Access')]").click()
child_windows=driver.window_handles
for window in child_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        email=driver.find_element(By.XPATH,"//a[contains(text(),'mentor')]").text
        driver.close()
driver.switch_to.window(parent_window)
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,'password').send_keys("admin")
driver.find_element(By.ID,'signInBtn').click()
wait=WebDriverWait(driver,10)
print(wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'div .alert'))).text)

