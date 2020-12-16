from bs4 import BeautifulSoup

with open("C:\Users\Owner1\Desktop\GMIT\Data Representation\Carviewer.html") as fp: soup  = BeautifulSoup(fp, 'html.parser')

print(soup1.prettify())