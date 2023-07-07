
from __future__ import absolute_import, unicode_literals
import random 

from celery import shared_task
from django.core.management import call_command
import sys

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
from celery import shared_task
import tweepy
import re
import datetime
from dateutil import parser

base_url = "https://twitterpricebot.onrender.com"


client = tweepy.Client(

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMBQogEAAAAAy81Zg8iD%2FkJLn4vtu6lKC2iZHio%3D3ZDBLLkvYSEIBnYl4hUIrOMb0k1dJSqvL0ezC863F5MLzCLMTq',
consumer_key = '4QRRwAkTZj3WYljLxMegSZKNy',
consumer_secret = 'DxKsIYPPISyMR7BjX31ydPOCKKV63fLQmQiq5FIqp23xW9ctV3',
access_token = '1675806484028858368-5CREsq4t1agimjIKDZvIPfXXgFz0Za',
access_token_secret = 'lRGE0rZOkpshLlKdF4ufAbA6IfBcJwD93a4EeXZyRnDAp'

)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
#tasks
@shared_task
def crypto_scraper(url):
    driver = Chrome(chrome_options=chrome_options, executable_path = "C:/Users/USER/desktop/SerialBuilds/pricebot/backend/pricebot/chromedriver.exe")
    driver.get(url)
    delay = 120

    try:
        data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-zo19gu')))
        

        print(data.text)
        return data.text
        #print(price.text)
    except TimeoutException:
        print ("sorry,data not available")

@shared_task
def stock_scraper(url):
    driver = Chrome(chrome_options=chrome_options, executable_path = "C:/Users/USER/desktop/SerialBuilds/pricebot/backend/pricebot/chromedriver.exe")
    driver.get(url)
    delay = 120

    try:
        data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'fxKbKc')))
        

        print(data.text)
        return data.text
        #print(price.text)
    except TimeoutException:
        print ("sorry,data not available")





### currency exchange rates
@shared_task
def exchange_rate_scraper(url):
    driver = Chrome(chrome_options=chrome_options, executable_path = "C:/Users/USER/desktop/SerialBuilds/pricebot/backend/pricebot/chromedriver.exe")
    driver.get(url)
    delay = 120

    try:
        data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'fxKbKc')))
        

        print(data.text)
        return data.text
        #print(price.text)
    except TimeoutException:
        print ("sorry,data not available")






@shared_task
def exchange_rates():
    dollar_url = f"{base_url}/results/get-dollar-data"
    dollar_response = requests.get(dollar_url)
    dollar_result = dollar_response.json()["result"]
    dollar_result = re.sub(r'["]', '', dollar_result)

    euro_url = f"{base_url}/results/get-euro-data"
    euro_response = requests.get(euro_url)
    euro_result = euro_response.json()["result"]
    euro_result = re.sub(r'["]', '', euro_result)

    pound_url = f"{base_url}/results/get-pound-data"
    pound_response = requests.get(pound_url)
    pound_result = pound_response.json()["result"]
    pound_result = re.sub(r'["]', '', pound_result)

    date_time = pound_response.json()["date_done"]
    date_time = parser.parse(date_time)
    date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")

    data_dict = {
        "Dollar": dollar_result,
        "Euro": euro_result,
        "Pound": pound_result
    }

    results = f"EXCHANGE RATES UPDATE - {date_time} \n \n Dollar: GHS {dollar_result}\n \n Euro: GHS {euro_result}\n \n Pound: GHS {pound_result} \n"

    client.create_tweet(text=results)

    print(results)
    return results


@shared_task
def cryptos():
    bitcoin_url = f"{base_url}/results/get-bitcoin-data"
    bitcoin_response = requests.get(bitcoin_url)
    bitcoin_result = bitcoin_response.json()["result"]
    bitcoin_result = re.sub(r'["]', '', bitcoin_result)

    cardano_url = f"{base_url}/results/get-cardano-data"
    cardano_response = requests.get(cardano_url)
    cardano_result = cardano_response.json()["result"]
    cardano_result = re.sub(r'["]', '', cardano_result)

    dogecoin_url = f"{base_url}/results/get-dogecoin-data"
    dogecoin_response = requests.get(dogecoin_url)
    dogecoin_result = dogecoin_response.json()["result"]
    dogecoin_result = re.sub(r'["]', '', dogecoin_result)

    bnb_url = f"{base_url}/results/get-bnb-data"
    bnb_response = requests.get(bnb_url)
    bnb_result = bnb_response.json()["result"]
    bnb_result = re.sub(r'["]', '', bnb_result)

    ethereum_url = f"{base_url}/results/get-ethereum-data"
    ethereum_response = requests.get(ethereum_url)
    ethereum_result = ethereum_response.json()["result"]
    ethereum_result = re.sub(r'["]', '', ethereum_result)

    date_time = ethereum_response.json()["date_done"]
    date_time = parser.parse(date_time)
    date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")



    results = f"CRYPTO PRICES UPDATE - {date_time} \n \n Bitcoin: {bitcoin_result}\n \n Cardano: {cardano_result} \n \n Dogecoin: {dogecoin_result}\n \n BNB: {bnb_result}"

    client.create_tweet(text=results)

    print(results)
    return results



@shared_task
def stocks():
    apple_stock_url = f"{base_url}/results/get-apple-data"
    apple_stock_response = requests.get(apple_stock_url)
    apple_stock_result = apple_stock_response.json()["result"]
    apple_stock_result = re.sub(r'["]', '', apple_stock_result)

    google_stock_url = f"{base_url}/results/get-google-data"
    google_stock_response = requests.get(google_stock_url)
    google_stock_result = google_stock_response.json()["result"]
    google_stock_result = re.sub(r'["]', '', google_stock_result)

    microsoft_stock_url = f"{base_url}/results/get-microsoft-data"
    microsoft_stock_response = requests.get(microsoft_stock_url)
    microsoft_stock_result = microsoft_stock_response.json()["result"]
    microsoft_stock_result = re.sub(r'["]', '', microsoft_stock_result)

    tesla_stock_url = f"{base_url}/results/get-tesla-data"
    tesla_stock_response = requests.get(tesla_stock_url)
    tesla_stock_result = tesla_stock_response.json()["result"]
    tesla_stock_result = re.sub(r'["]', '', tesla_stock_result)

    meta_stock_url = f"{base_url}/results/get-meta-data"
    meta_stock_response = requests.get(meta_stock_url)
    meta_stock_result = meta_stock_response.json()["result"]
    meta_stock_result = re.sub(r'["]', '', meta_stock_result)

    amazon_stock_url = f"{base_url}/results/get-amazon-data"
    amazon_stock_response = requests.get(amazon_stock_url)
    amazon_stock_result = amazon_stock_response.json()["result"]
    amazon_stock_result = re.sub(r'["]', '', amazon_stock_result)

    date_time = amazon_stock_response.json()["date_done"]
    date_time = parser.parse(date_time)
    date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")



    results = f"STOCK PRICES UPDATE - {date_time} \n \n Apple: {apple_stock_result}\n \n Google: {google_stock_result} \n \n Microsoft: {microsoft_stock_result}\n \n Meta: {meta_stock_result} \n \n Tesla: {tesla_stock_result}"

    client.create_tweet(text=results)

    print(results)
    return results

