from selenium import webdriver

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("headless")
option.add_argument("--ignore-certificate-errors") #this will ignore certification issue
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#executor
#document.body.scrollHeight - get whole page height
#driver.execute_script("window.scrollTo(0,600)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")