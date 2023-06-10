import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params = {
    'serviceKey' : 'bSzFPEUSrutyp2hUNcap3hiuUVNfADtwGmK3C68jTWWT5E9YrgVJK2yldsBHCy1DSZX+AA0vas6W1FZLImBtHA==',
    'returnType' : 'xml',
    'numOfRows' : '100',
    'pageNo' : '1',
    'year' : '2020',
    'itemCode' : 'PM10'
}

response = requests.get(url, params=params)
decoded_content = response.content.decode('utf-8')



# Parse the XML data
root = ET.fromstring(decoded_content)

# Find all the item elements
items = root.findall('.//item')



# Iterate over items and check issueGbn
index = 1
for item in items:
    district_name = item.find('districtName').text
    issue_val = item.find('issueVal').text

    # Check if districtName is "경기" and print issueVal with index
    if district_name == '경기':
        print(f"{index}: {issue_val}")
        index += 1