import requests
from datetime import datetime

id = '1d4cba4a-72d3-4641-9cea-9c2a6ffbf16c'
packet = {'UserTypeCode':'HCK', 'Name':'bob banana', 'School':'Ukeley', 'Major':'Feminist Studies', 'Street1':'high street', 'Street2':'test', 'City':'santa cruz', 'StateCode':'CA', 'ZipCode':95064, 'CountryCode':'US', 'Phone':'123-456-7890', 'Email':'test@ucsc.edu', 'BirthDate':datetime.now(), 'ProfileImageUrl':None}


print(requests.post('http://localhost:8080/hackers', packet).json())
print(requests.get('http://localhost:8080/hackers/' + id).json())
print(requests.put('http://localhost:8080/hackers/' + id, packet).json())
print(requests.delete('http://localhost:8080/hackers/' + id).json())

print(requests.get('http://localhost:8080/hackers/' + id).json())