import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
# suggestionlist=driver.find_elements(By.XPATH,"//form[@id='aspnetForm']/following::ul[1]/li/a")
# print(len(suggestionlist))
# for i in suggestionlist:
#     print(i.text)

sugestionlist=driver.find_elements(By.CSS_SELECTOR,'li[class="ui-menu-item"] a')
print(len(sugestionlist))
for i in sugestionlist:
    # print(i.text)
    if i.text == "India":
        i.click()
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))