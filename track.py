import time
import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Canon-spiegellose-F4-5-6-3-Hybridkamera-Fokussystem/dp/B0B88KB624/ref=sxin_36_hcs-la-eu-prod?content-id=amzn1.sym.d4689940-c641-4973-9d48-36b7cacdaf68%3Aamzn1.sym.d4689940-c641-4973-9d48-36b7cacdaf68&crid=23DAZC53D4G63&cv_ct_cx=canon+kamera&keywords=canon+kamera&pd_rd_i=B0B88KB624&pd_rd_r=f0f716ff-24a2-4e67-8a00-ff4c15b232d1&pd_rd_w=CXsxJ&pd_rd_wg=nEjnO&pf_rd_p=d4689940-c641-4973-9d48-36b7cacdaf68&pf_rd_r=JJMAJN253QGMF40EBMDH&qid=1667764406&sprefix=canon%2Caps%2C147&sr=1-2-b2e13ad2-9722-4958-922a-611dd835899b'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(URL , headers=headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    #title = soup.find(id='productTitle').get_text()
    price =soup.find('span', class_=['a-offscreen']).get_text()
    converted = float(price[0:5])

    if(converted<1.700):
        send_email()

    print(converted)
    if(converted>1.700):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('YOUR_Email','Your_Password')

    subject ='Price fell down'
    body = 'check the amazon link'
    msg =f"subject:{subject}\n\n{body}"

    server.sendmail(
        'FROM--> Email',
        'TO--> Email',
        msg
    )
    print('Hey Email Has Been Sent')
    server.quit()

while(True):
    check_price()
    time.sleep(86400)

