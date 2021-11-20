from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import logging


def botify():

    # ======= Setting =============
    # Your daft credentials
    email = "Your Email"
    password = "Your password"

    # Initiate the browser
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    chrome_driver_binary = "/usr/bin/chromedriver"
    browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    logging.info("initating the browser!")

    # open the site
    browser.get('https://www.daft.ie/property-for-rent/galway-city')

    # Accept Terms
    browser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').click()
    
    # Find and click sign in
    browser.find_element_by_xpath('//*[@id="__next"]/header/div/div[2]/div[3]/ul/li[2]/a').click()

    # credentials
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(email)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    # click
    browser.find_element_by_xpath('//*[@id="kc-login-form"]/div[2]/input').click()
