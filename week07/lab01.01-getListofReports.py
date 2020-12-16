import requests
import json


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json()

listOfReports = []
#output to console
#print (data) # cannot get date function to work in the parameters
for item in data["items"]:#this is all in a list, if there is multiple pages it can get more complicated
    #print(item["ResourceName"])#prints out the item resource names
    listOfReports.append(item["ResourceName"])

for ReportName in listOfReports:
    print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName#add on the information you need
    print(url)
    response= requests.get(url)
    aReport= response.json() #each on the reports

#other code
#save this to a file
filename = 'allreports.json'
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)