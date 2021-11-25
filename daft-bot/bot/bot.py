#!/usr/bin/python

from models import model
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup, element
import datetime

import message


Houses_Visited = {}
email = ""
password = ""


def botify():

    # Initiate the browser
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    chrome_driver_binary = "/usr/bin/chromedriver"
    browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    # open the site
    browser.get(
        'https://www.daft.ie/property-for-rent/galway-city?rentalPrice_to=1500&rentalPrice_from=500&sort=publishDateDesc')

    # Accept Terms
    browser.find_element_by_xpath(
        '//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').click()

    # sign_in(browser)
    scrape(browser)


def sign_in(browser):

    # # Find and click sign in
    # # ========================
    browser.find_element_by_xpath(
        '//*[@id="__next"]/header/div/div[2]/div[3]/ul/li[2]/a').click()

    # # Credentials
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(email)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    # # Click
    browser.find_element_by_xpath(
        '//*[@id="kc-login-form"]/div[2]/input').click()
    # # ========================


def sendMail(house, browser):
    fullUrl = "https://www.daft.ie" + house.url
    print(fullUrl)

    # navigate to house page
    browser.get(fullUrl)

    # Click Email
    email_button = browser.find_elements_by_class_name(
        "NewButton__StyledButton-yem86a-2")[3]

    email_button.click()

    # Scrape Name
    # print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id="contact-form-modal"]/div[2]/div[2]/div/div[2]/p[1]"))).text)

    content = browser.page_source
    smallSoup = BeautifulSoup(content, features="html.parser")
    letterName = smallSoup.find(
        "p", {"class": "ProfileOverview__BoldText-x27s1t-5"}).text

    # Generate Message
    gen_msg = message.generate(letterName, house.address)

    # Fill Details
    full_name_input = "First last"
    message_email_input = "email.mail"
    phone_input = "123456"

    browser.find_elements_by_class_name(
        "TermsFilter__StyledInput-sc-12tisn1-4")[0].send_keys(full_name_input)
    browser.find_elements_by_class_name(
        "TermsFilter__StyledInput-sc-12tisn1-4")[1].send_keys(message_email_input)
    browser.find_elements_by_class_name(
        "TermsFilter__StyledInput-sc-12tisn1-4")[2].send_keys(phone_input)
    browser.find_element_by_class_name(
        "TextArea__StyledTextarea-usffhd-1").send_keys(gen_msg)
    # browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div/div[5]/div/button').click() # careful now!


def scrape(browser):
    content = browser.page_source
    soup = BeautifulSoup(content, features="html.parser")

    for house_scrape in soup.findAll('li', attrs={'class': 'SearchPage__Result-gg133s-2 itNYNv'}):

        house = model.House("", "", "", "")
        # house.timestamp =
        house.price = house_scrape.find(
            "span", {"class": "TitleBlock__StyledSpan-sc-1avkvav-4 gDBFnc"}).text
        house.address = house_scrape.find(
            "p", {"class": "TitleBlock__Address-sc-1avkvav-7"}).text
        el = house_scrape.find(href=True)
        house.url = el['href']

        current_time = datetime.datetime.now()
        house.date = str(current_time.timestamp())

        if house.address not in Houses_Visited:
            sendMail(house, browser)
            Houses_Visited[house.address] = house
