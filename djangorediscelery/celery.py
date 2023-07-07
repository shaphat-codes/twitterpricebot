import os 
from celery import Celery
from decouple import config
from bot.make_requests import *
from celery.schedules import crontab
import ssl


#set default django settings module for the celery program

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorediscelery.settings')

app = Celery('djangorediscelery', BROKER_USE_SSL={'ssl_cert_reqs': ssl.CERT_REQUIRED})

app.config_from_object('django.conf:settings', namespace='CELERY')


#LOAD TASK MODULES FROM ALL REGISTERED DJANGO APP CONFIGS
app.autodiscover_tasks()

# Scheduler
bitcoin_url = "https://www.binance.com/en/price/bitcoin"
ethereum_url = "https://www.binance.com/en/price/ethereum"
dogecoin_url = "https://www.binance.com/en/price/dogecoin"
bnb_url = "https://www.binance.com/en/price/bnb"
cardano_url = "https://www.binance.com/en/price/cardano"

google_stock_url = "https://www.google.com/finance/quote/GOOGL:NASDAQ?hl=en"
apple_stock_url = "https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en"
microsoft_stock_url = "https://www.google.com/finance/quote/MSFT:NASDAQ?hl=en"
amazon_stock_url = "https://www.google.com/finance/quote/AMZN:NASDAQ?hl=en"
meta_stock_url = "https://www.google.com/finance/quote/META:NASDAQ?hl=en"
tesla_stock_url = "https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en"

dollar_rate_url = "https://www.google.com/finance/quote/USD-GHS?hl=en"
euro_rate_url = "https://www.google.com/finance/quote/EUR-GHS?hl=en"
pound_rate_url = "https://www.google.com/finance/quote/GBP-GHS?hl=en"

crypto_urls = [bitcoin_url, ethereum_url, dogecoin_url, bnb_url, cardano_url]
stock_urls =  [google_stock_url, apple_stock_url, microsoft_stock_url, amazon_stock_url, meta_stock_url, tesla_stock_url]
exchange_rate_urls = [dollar_rate_url, euro_rate_url, pound_rate_url]




app.conf.beat_schedule = {
            'get-bitcoin-data': {
                'task': 'bot.tasks.crypto_scraper',
                'schedule': 2000,
                'args': [bitcoin_url],
            },

            'get-ethereum-data': {
                'task': 'bot.tasks.crypto_scraper',
                'schedule': 2000,
                'args': [ethereum_url],
            },
            'get-bnb-data': {
                'task': 'bot.tasks.crypto_scraper',
                'schedule': 2000,
                'args': [bnb_url],
            },
            'get-cardano-data': {
                'task': 'bot.tasks.crypto_scraper',
                'schedule': 2000,
                'args': [cardano_url],
            },
            'get-dogecoin-data': {
                'task': 'bot.tasks.crypto_scraper',
                'schedule': 2000,
                'args': [dogecoin_url],
            },
            'get-google_stock-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [google_stock_url],
            },
            'get-amazon_stock-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [amazon_stock_url],
            },
            'get-apple_stock-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [apple_stock_url],
            },
            'get-meta-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [meta_stock_url],
            },
            'get-tesla-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [tesla_stock_url],
            },
            'get-microsoft-data': {
                'task': 'bot.tasks.stock_scraper',
                'schedule': 2000,
                'args': [microsoft_stock_url],
            },
            
             'get-dollar-data': {
                'task': 'bot.tasks.exchange_rate_scraper',
                'schedule': 2000,
                'args': [dollar_rate_url],
            },
             'get-pound-data': {
                'task': 'bot.tasks.exchange_rate_scraper',
                'schedule': 2000,
                'args': [pound_rate_url],
            },
             'get-euro-data': {
                'task': 'bot.tasks.exchange_rate_scraper',
                'schedule': 2000,
                'args': [euro_rate_url],
            },



            'get-cryptos-data': {
                'task': 'bot.tasks.cryptos',
                'schedule': 20000,
                
            },

            'get-stocks-data': {
                'task': 'bot.tasks.stocks',
                'schedule': 20000,
                
            },

            'get-exchange_rates-data': {
                'task': 'bot.tasks.exchange_rates',
                'schedule': 20000,
                
            },

            


            
            
            
    }
