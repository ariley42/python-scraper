import requests
from bs4 import BeautifulSoup
import smtplib, ssl


URL = 'https://www.amazon.com/Acer-Aspire-i5-8250U-GeForce-E5-576G-5762/dp/B075FLBJV7/ref=sr_1_9?crid=5VCLGO76NUPO&keywords=linux+laptop&qid=1569023484&s=gateway&sprefix=linux+lap%2Caps%2C232&sr=8-9'

headers = {"User-Agent": 'Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36'}

def check_price():
    
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'lxml')


    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    prices = price.strip('$')

    converted_price = float(price[1:5])

    if(converted_price < 7.00):
        send_mail()

    print(converted_price)

    print(title.strip())
    
 
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(
        # your login info here
        )
    msg = """\Subject:Price went down
    
    
    Check the amazon link https://www.amazon.com/Acer-Aspire-i5-8250U-GeForce-E5-576G-5762/dp/B075FLBJV7/ref=sr_1_9?crid=5VCLGO76NUPO&keywords=linux+laptop&qid=1569023484&s=gateway&sprefix=linux+lap%2Caps%2C232&sr=8-9"""
    
    
    
   
    # Send yourself an email here
        
    print('Email has been sent!!!')
    
    
check_price()

