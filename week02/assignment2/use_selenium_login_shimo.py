from selenium import webdriver
import time


url = "https://shimo.im/login?from=home"
username = 'test123'
password = 'test123'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(password)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    browser.close()