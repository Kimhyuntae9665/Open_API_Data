import requests

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : 'bSzFPEUSrutyp2hUNcap3hiuUVNfADtwGmK3C68jTWWT5E9YrgVJK2yldsBHCy1DSZX+AA0vas6W1FZLImBtHA==', 'returnType' : 'xml', 'numOfRows' : '1', 'pageNo' : '1', 'year' : '2020', 'itemCode' : 'PM10' }

response = requests.get(url, params=params)
print(response.content)