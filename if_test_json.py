import requests
import json

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params = {
    'serviceKey' : 'bSzFPEUSrutyp2hUNcap3hiuUVNfADtwGmK3C68jTWWT5E9YrgVJK2yldsBHCy1DSZX+AA0vas6W1FZLImBtHA==',
    'returnType' : 'json',
    'numOfRows' : '100',
    'pageNo' : '1',
    'year' : '2020',
    'itemCode' : 'PM10'
}

response = requests.get(url, params=params)
data = response.json()
# ? data 항목에서 response,body,items 항목에 접근 하는 것 더 더 안으로 접근하는 느낌 
items = data['response']['body']['items']

# Iterate over items and check districtName
index = 1
for item in items:
    district_name = item['districtName']
    issue_val = item['issueVal']

    # Check if districtName is "경기" and print issueVal with index
    if district_name == '경기':
        print(f"{index}: {issue_val}")
        index += 1