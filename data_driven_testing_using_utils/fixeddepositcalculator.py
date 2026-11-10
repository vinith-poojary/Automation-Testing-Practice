import time

import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import excelutils

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycntrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\Menu\\exc1.xl.xlsx"
rows=excelutils.getRowcount(file,"sheet1")

for r in range(2,rows+1):
    pric=excelutils.readData(file,"sheet1",r,1)
    rateofintrset=excelutils.readData(file,"sheet1",r,2)
    par1=excelutils.readData(file,"sheet1",r,3)
    par2=excelutils.readData(file,"sheet1",r,4)
    fre=excelutils.readData(file,"sheet1",r,5)
    exp_mvalue=excelutils.readData(file,"sheet1",r,6)

    #passing data to the application

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='intrest']").send_keys(rateofintrset)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(par1)

    perioddrp=select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_visible_text(par2)

    frequency=select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequency.select_visible_text(fre)

    driver.find_element(By.XPATH,"//select[@id='fdMatVal']/div[2]/a[1]/img").click()

    act_value=driver.find_element((By.XPATH,"//span[@id='resp_matval']/strong")).text


    #validation
    if float(exp_mvalue)==float(act_value):
        print("text passed")
        excelutils.writeData(file,"sheet1",r,8,"passed")
        excelutils.fillGreenColor(file,"sheet1",r,8)

    else:
        print("text failed")
        excelutils.writeData(file,"sheet1",r,8,"failed")
        excelutils.fillRedcolor(file,"sheet1",r,8)

    driver.find_element(By.XPATH,"//*[@id='foMatVal']/div[2]/a[2]/img").click()
