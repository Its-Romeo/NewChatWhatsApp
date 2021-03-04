#WhatsappNewChat

This app will send bulk messages to unsaved numbers on the whatsapp. It will take numbers from excel file, message from a text file and it will keep sending the messages. It will skip any numbers that is not registered on the whatsapp.  

Requirments:
Install all these Requirments
1) Python 3
2) Selenium
3) Chrome Webdriver according to your Chrome version

How To Use:
1) Goto https://chromedriver.chromium.org/downloads and download webdriver for chrome according to your chrome version.
2) Copy webdriver to driver folder inside this project.
3) Copy your xlsx file containing phone numbers to files directory inside this project.
4) Copy your text file containing you message to files directory inside this project.

Note: Make sure that the name of column containing numbers is "number" exactly, otherwise it will not work.

5) Open cmd or terminal if you are on linux and navigate inside WhatsappNewChat then type python wa.py or python3 wa.py if you are on linux.
6) Hit enter and then chrome will load the whatsapp web, scan the code and you are good to go. 
