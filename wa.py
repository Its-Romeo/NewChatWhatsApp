# ***************************************************************************************/
# *    Title: WhatsappNewChat
# *    Author: Romeo
# *    Date: 2021
# *    Code version: 1.0
# *    Availability: 
# *
# ***************************************************************************************/


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as PD

# Please change file paths in line number 12, 13 and 14 according to your own file paths

driver_path = 'chrome driver path here'# Put driver path here
excel_path = 'chrome driver path here/file.xlsx' # Put Excel path here
message = 'chrome driver path here/msg.txt'          # Put message file path here   

#set chrome options 
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  
chrome_options.add_argument('--disable-notifications')      #disable popups
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--start-maximized')
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options, executable_path= driver_path)

wait = WebDriverWait(driver, 60)
wait2 = WebDriverWait(driver, 10)

#read message from text file
f = open(message, 'r', encoding='utf8')
msg_text = f.read()
msgs = msg_text.split('\n')

#read numbers from xlsx file
df = PD.read_excel(excel_path)
number = df['number'].tolist() # the file must have phone numbers under column name 'number', othervise change it here 
count = 1

for i in number:
    try:
        # method 'switch_to_alert()' is not working in some cases, if so change it to 'switch_to.alert()'
        alrt = driver.switch_to_alert()
        alrt.accept()
        print ("alert accepted")
    except:
        print ("no alert")

    contact = f'https://web.whatsapp.com/send/?phone=/{str(i)}'
    driver.get(contact)
    time.sleep(5) 
    try:
        # method 'switch_to_alert()' is not working in some cases, if so change it to 'switch_to.alert()'
       alrt = driver.switch_to_alert()
       alrt.accept()
       print ("alert accepted")
    except:
        print ("no alert")
    time.sleep(5) 
        
    try:   
        chat_box = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        for msg in msgs:
            chat_box.send_keys(msg)
            chat_box.send_keys(Keys.SHIFT,'\n')
        chat_box.send_keys("\n")   
        print(f'Message sent to {str(i)}') 

        time.sleep(3)  
        count+=1 
        print(f'{count} messages sent')
    except: 
        print(f'{str(i)} is not awailable on WahtsApp') 
    time.sleep(5)  

    try:        
        alert = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')))
        alert.click()
    except:
        print('checking next number')  