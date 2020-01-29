import requests
from bs4 import BeautifulSoup
import stmplib
import time

URL = 'https://www.amazon.ca/Tile-Inc-RE-25004-Sticker-4-pack/dp/B07W4XYTPY?ref_=MWishedForC&pf_rd_r=R7WZ8BFV0VMQS5BZB2X1&pf_rd_p=513fe281-9dd6-5881-ab66-6b9530cf0344&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=667823011&pf_rd_m=A3DWYIK6Y9EEQB'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' }

def check_price():
	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find(id = "productTitle").get_text()
	price = soup.find(id = "priceblock_ourpirce").get_text()
	converted_price = float(price[0:5])
	if(converted_price < 40.000):
		send_mail()
	
	print(converted_price)
	print(title.strip()) 

	if(converted_price < 40.000):
		send_mail()

def send_mail():
	server = stmplib.SMTP('smpt.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('vardansawhney@gmail.com', 'FILL IN WITH PASSWORD')
	subject = 'Price dropped !'
	body = 'Check the link: https://www.amazon.ca/Tile-Inc-RE-25004-Sticker-4-pack/dp/B07W4XYTPY?ref_=MWishedForC&pf_rd_r=R7WZ8BFV0VMQS5BZB2X1&pf_rd_p=513fe281-9dd6-5881-ab66-6b9530cf0344&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=667823011&pf_rd_m=A3DWYIK6Y9EEQB'

	msg = f"Subject: {subject}\n\n{body}"
	server.sendmail(
		'vardansawhney@gmail.com', 'vardansawhney@gmail.com', msg)

	print('SENT')
	server.quit()

while(true):
	check_price()
	time.sleep(3600)
