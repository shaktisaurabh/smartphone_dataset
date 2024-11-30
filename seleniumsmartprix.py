from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 
import undetected_chromedriver as uc 

driver=uc.Chrome()
driver.get('https://www.smartprix.com/mobiles')

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(4)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(2) 
old_height=driver.execute_script('return document.body.scrollHeight')
time.sleep(2)
while True:
    driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    print(old_height,new_height)
    if old_height==new_height:
        break
    old_height=new_height 
html=driver.page_source 
with open('smartprix2.html','w',encoding='utf-8') as f:
    f.write(html) 

input("Press Enter to close the browser...")  # Keeps the browser open until you press Enter

# Close the browser when done
driver.quit()




