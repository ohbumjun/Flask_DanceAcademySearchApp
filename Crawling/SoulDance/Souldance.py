import requests
from urllib.error import HTTPError
from PIL import Image
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd


# 1. 웹페이지 분석 : url
url = "https://calendar.google.com/calendar/htmlembed?height=600&wkst=1&bgcolor=%23ffffff&ctz=Asia%2FSeoul&src=b2szMXI4amQ2c3VmNGp1azd0dW5zOXRxZW9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23878787&showTitle=0&showPrint=0&showCalendars=0&mode=AGENDA"
headers = {
    "user-agent" :UserAgent().chrome ,
    "referer" : "https://souldance.kr/class"
}

response = requests.get(url, headers = headers)

# 이미지 불러오기
# im = Image.open('C:/Users/user/Desktop/Web_Study/Dance_Match/Image/SoulDance/SoulDance.png')

# print(response)

dom = BeautifulSoup(response.content, "html.parser")
# print(dom.text)

Days = dom.select( "body > div.view-container-border > div > div.date-section")
# print(len(Days))

# # 요일
# Days[0].select_one(".date").text.split(" ")[3].split("(")[1].split(")")[0]

# # 수업 시간
# Classes = Days[0].select("tr")
# print(len(Classes))
# print(Classes[0].select_one("td:first-child").text)

# # 수업 정보 : 수업 이름 
# Classes[0].select_one("td:nth-child(2)").text



Soul_Classes = []

for a in range(0, len(Days)):
    Classes = Days[a].select("tr")
    for i in range(0, len(Classes)):
        Soul_Classes.append({
                                'Academy_Name': 'SoulDance' ,
                                'Class_Names': Classes[i].select_one("td:nth-child(2)").text ,
                                'Day_1': "WeekDay" ,
                                'Day_2': Days[a].select_one(".date").text.split(" ")[3].split("(")[1].split(")")[0] , 
                                'Time_1': "Night" ,
                                'Time_2': Classes[i].select_one("td:first-child").text  ,
                                'Genre': "Choreography" ,
                                'Link': "https://souldance.kr/" ,
                                'Place': "서울시 동작구 사당로 30길 164, 2F",
                                'Contact': "02-523-1933" ,
                                'NumOfClass': 1 ,
                                "District": "Dongjak" ,
                                "Img" : "https://cdn.imweb.me/thumbnail/20200323/253cccb04dd95.png"
                            })

print(len(Soul_Classes))

Soul_Classes_DF = pd.DataFrame(Soul_Classes)

print(type(Soul_Classes_DF))
Soul_Classes_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Soul.csv", mode = "w", encoding="utf-8")

