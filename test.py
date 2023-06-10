import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : 'bSzFPEUSrutyp2hUNcap3hiuUVNfADtwGmK3C68jTWWT5E9YrgVJK2yldsBHCy1DSZX+AA0vas6W1FZLImBtHA==', 
         'returnType' : 'xml', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'year' : '2020', 
         'itemCode' : 'PM10' }

response = requests.get(url, params=params)
decoded_content = response.content.decode('utf-8')
# print(decoded_content);

# Parse the XML data
root = ET.fromstring(decoded_content)

# Find all the item elements
# ? 먼저 인스턴스 하나하나를 감싸고 있는 item을 먼저 가져온다 ==> 인스턴스 단위로 먼저 나눈다 
items = root.findall('.//item')
# print(items);

# Extract districtName elements from the first 10 items
district_names = [item.find('districtName').text for item in items[:int(params['numOfRows'])]]

# Print the district names
for i, district_name in enumerate(district_names, start=1):
    print(f"{i}: {district_name}")



# root = ET.fromstring(decoded_content)

# #특정 element 추출
# district_name = root.find('.//districtName').text
# issue_gbn = root.find('.//issueGbn').text

# print(f"districtName: {district_name}")
# print(f"issueGbn: {issue_gbn}")