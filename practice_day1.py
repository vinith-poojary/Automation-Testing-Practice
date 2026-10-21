from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

#open particular browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#this which is used to perform double click
var=driver.find_element(By.XPATH,"//*[@id='field1']")
var.clear()
var.send_keys("tester")

button=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
act=ActionChains(driver)
act.double_click(button).perform()


driver.implicitly_wait(10)


#this which is used for drag and drop the element
dr=driver.find_element(By.XPATH,"//*[@id='draggable']/p")
tr=driver.find_element(By.XPATH,"//*[@id='droppable']")
act=ActionChains(driver)
act.drag_and_drop(dr,tr).perform()
time.sleep(5)

#used for the slider through locators
min_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print(min_slider.location)
print(max_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,39,0).perform()
act.drag_and_drop_by_offset(max_slider,256,0).perform()
print(min_slider.location)
print(max_slider.location)


#scroll down to end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels moved:",value)
time.sleep(5)



#scroll up from bottom of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels moved:",value)
time.sleep(5)

#click link

driver.find_element(By.XPATH,"//*[@id='broken-links']/a[3]").click()
time.sleep(5)
