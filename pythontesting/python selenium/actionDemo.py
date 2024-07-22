from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"mousehover")
action=ActionChains(driver)
#context_click() - right click
#drag and drop()
action.click_and_hold(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()