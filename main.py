import selenium
import time
from random import seed, random
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

username = input("Enter Username: ")
password = input("Enter Password: ")
search = input("Enter a hashtag: ")
print ("Please Wait While Instagram Loads...")

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(3)
username_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
password_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")

username_input.send_keys (username)
password_input.send_keys (password)

login_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
login_button.click()

sleep(6)
search_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]/div/div/span/span")
search_button.click()

sleep(2)
search_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
search_input.send_keys(search)

hashtag_follow = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/div/span")
hashtag_follow.click
sleep(20)

browser.quit()
print("Thank You")
