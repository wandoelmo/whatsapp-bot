from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import io

def getQrCode(driver):
    print('Getting QR Code...')
    #Finds the QRCode position
    src = driver.find_element_by_tag_name('img')
    #Gets its BAse64 value
    qrCode = src.get_attribute('src').replace("data:image/png;base64,","")
    print('Generating HTML page...')
    with open('test.html', 'w') as f:
        f.write('<html><head><title>QR Code</title></head><body>\n')
        f.write('<img src="data:image/png;base64,{}">\n'.format(qrCode))
        f.write('</body></html>')
