from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
curr_window=driver.current_window_handle
driver.find_element(By.LINK_TEXT,"Click Here").click()
window_handles=driver.window_handles
for i in window_handles:
    if i != curr_window:
        driver.switch_to.window(i)
        print(driver.title)
        driver.close()
driver.switch_to.window(curr_window)
print(driver.title)
