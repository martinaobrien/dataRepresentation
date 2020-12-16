from bs4 import BeautifulSoup

with open("..\Week 3\Carviewer.html") as fp:
    soup  = BeautifulSoup(fp, 'html.parser')

#print (soup.tr)

rows = soup.findAll("tr")
for row in rows:
    #print(row)
    datalist = []
    cols =row.findAll('td')
    for col in cols:
        datalist.append(col.text)
    print(datalist)