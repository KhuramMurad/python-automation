import requests
url =r"https://hdfcbankdev.service-now.com/api/hdfcb/ibm_ro_incident/newIncident"
user="IBM_RO_User"
password=r"r<U#44v>-mF:^%l%L46SFo>5@9qhXxQ:Dvf[uo<N"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
response= requests.post(url,auth=(user,password),headers=headers)

if response.status_code !=200:
    print("Status:",response.status_code,'Headers:',response.headers,'Error Response:',response.json())
    exit()
data= response.json()
print(data)