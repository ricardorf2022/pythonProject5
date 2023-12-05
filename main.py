
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

username_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
password_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")

username_input.send_keys("") #enter username
password_input.send_keys("") #enter password

login_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
login_button.click()

sleep(5)

