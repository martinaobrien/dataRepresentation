import requests
import csv
from bs4 import BeautifulSoup
url= "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
page = requests.get(url)

soup - BeautifulSoup(page.content, 'html.parser')

home_file = open('week03myhome.csv' , mode = 'w')
home_writer= csv.writer(home_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAl)
listings = soup.findAll("div",class_="PropertyListingCard")

for listing in listings:
    entryList = []

    price =listing.find(class_="PropertyListingCard_Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard_Address").text
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()