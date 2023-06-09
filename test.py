import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : 'bSzFPEUSrutyp2hUNcap3hiuUVNfADtwGmK3C68jTWWT5E9YrgVJK2yldsBHCy1DSZX+AA0vas6W1FZLImBtHA==', 'returnType' : 'xml', 'numOfRows' : '10', 'pageNo' : '1', 'year' : '2020', 'itemCode' : 'PM10' }

response = requests.get(url, params=params)
decoded_content = response.content.decode('utf-8')
# print(decoded_content);

# Parse the XML data
root = ET.fromstring(decoded_content)

# Find all the item elements
items = root.findall('.//item')

# Extract districtName elements from the first 10 items
district_names = [item.find('districtName').text for item in items[:10]]

# Print the district names
for district_name in district_names:
    print(district_name)



# root = ET.fromstring(decoded_content)

# #특정 element 추출
# district_name = root.find('.//districtName').text
# issue_gbn = root.find('.//issueGbn').text

# print(f"districtName: {district_name}")
# print(f"issueGbn: {issue_gbn}")