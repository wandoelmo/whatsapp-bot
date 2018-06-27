from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from getQrCode import getQrCode

def main():
    #Use chromewebdriver
    driver = webdriver.Chrome(r'/usr/bin/chromedriver')
    #Connect to WhatsApp
    driver.get('https://web.whatsapp.com')
    #Get the QR and saves it to a HTML file
    getQrCode(driver)
    #Wait for QR scan
    wait = WebDriverWait(driver = driver, timeout = 9000)
    #Ask for user input
    name = input('Enter the name of user or group : ')
    msg = input('Enter the message here: ')
    msg += '\n this is a system generated message'
    gotoChat(driver, name)
    sendMessage(driver, msg)
    webDriverQuit(driver)

def gotoChat(driver, name):
    #Finds target Chat/Group in HTML
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    #Clicks on it to select it
    user.click()

def sendMessage(msg):
    #Finds textbox in HTML
    msg_box = driver.find_element_by_class_name('_2S1VP')
    #Paste the message in the textbox
    msg_box.send_keys(msg)
    #Find the "send" button
    button = driver.find_element_by_class_name('_2lkdt')
    #Clicks the button and sends the message
    button.click()
    print('Sending message...')

def webDriverQuit():
    #Guess what? It quits
    driver.quit()
    print('Quitting...')
    quit()

if __name__ == "__main__":
    main()
