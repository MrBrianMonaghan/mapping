import selenium
from selenium import webdriver

try:
    browser = webdriver.Firefox()
    browser.get('mikekus.com')
except KeyboardInterrupt:
    browser.quit()
