import requests
import pandas as pd
# API URL 및 파라미터 설정

# contentTypeId 숙박 : 32 , 음식점 : 39, 문화시설 : 14
# 숙박 / 음식점 / 문화시설 별로 한번씩 반복 호출

contentTypeId = 39
url = "http://apis.data.go.kr/B551011/KorWithService1/areaBasedList1?" \
      "MobileOS=ETC&MobileApp=AppTest&_type=json&serviceKey=iMYSl6JaEtpLLmO1GPBk8gaukJpS9rHKQXfIUuXdrpZpjXy%2B%2BlvEY21gXPKgvR7CQtoLIjIGwVolxBZmtW5Q5w%3D%3D&areaCode=39&numOfRows=409" \
      f"&contentTypeId={contentTypeId}"

# API 호출
response = requests.get(url)
data = response.json()

# JSON 데이터에서 필요한 정보 추출
# 1차 크롤링 : content ID
items = data['response']['body']['items']['item']
filtered_items = [
    {"contentid": item["contentid"]}
    for item in items
]

# stroler

df = pd.DataFrame(columns=['babysparechair'])
print(df)

for item in filtered_items:
    ##print(item['contentid'])`
    url = "http://apis.data.go.kr/B551011/KorWithService1/detailWithTour1?MobileOS=ETC&MobileApp=AppTest" \
          "&contentId=" + str(item['contentid']) + "&serviceKey=o0kGvYO0CCAsOUZtnxd0lHtW6cGWNHSMTgFWRgr2%2F%2ByUV6G%2BBkUXMVsVamDh%2BbvEXVZdTwJyV6eLoeMToJM2RA%3D%3D&_type=json"

    # API 호출
    response = requests.get(url)
    data = response.json()
    print(data)
    # JSON 데이터에서 필요한 정보 추출
    # babySpareChair, parking, stroller 항목 수집 publictransport 수집 후 -> 유모차 접근가능으로 치환
    item_content = data['response']['body']['items']['item'][0]['babysparechair']
    df_tmp = pd.DataFrame([{'babysparechair': item_content}])
    print(df_tmp)
    df = pd.concat([df, df_tmp], ignore_index=True)


#df.to_csv('C://ai-jeju/dataset.csv')
#print(df)