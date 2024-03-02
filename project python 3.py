# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# Connect to Website and pull in data

URL = 'https://www.amazon.com/dp/B0B3BNL2H9/ref=sspa_dk_detail_1?pd_rd_i=B0B3BNL2H9&pd_rd_w=DkglP&content-id=amzn1.sym.0d1092dc-81bb-493f-8769-d5c802257e94&pf_rd_p=0d1092dc-81bb-493f-8769-d5c802257e94&pf_rd_r=N694XWSJV216G2JJWT4J&pd_rd_wg=4KhG3&pd_rd_r=cf6cd2df-0370-4eb7-bf83-3c7a365e9fbf&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title_element = soup2.find('span', id='productTitle')
title = title_element.get_text()
title = title_element.get_text(strip=True) if title_element else 'Title not found'

price_element = soup2.find('span', class_='a-price-whole')

price = price_element.get_text(strip=True) if price_element else 'Price not found'

 # Extract the product rating
rating_element = soup2.find('span', class_='reviewCountTextLinkedHistogram')
rating = rating_element['title'] if rating_element else 'Rating not found'
    
# Extract the number of reviews
reviews_element = soup2.find('span', id='acrCustomerReviewText')
reviews = reviews_element.get_text(strip=True) if reviews_element else 'Number of reviews not found'
    


print(f'title:{title}')
print(f'Price: {price}')
print(f'Rating: {rating}')
print(f'Number of reviews: {reviews}')
import csv

with open('product_data.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Price', 'Rating', 'Number of Reviews'])
        writer.writerow([title, price, rating, reviews])

print('Data has been saved to product_data.csv')
