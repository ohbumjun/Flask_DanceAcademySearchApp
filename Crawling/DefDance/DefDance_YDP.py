import requests
import pandas as pd
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from PIL import Image

# DB 세팅
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


# 공통 코드
url = "https://www.defcompany.com/defdance/sub_dance_01_02.html"

response = requests.get(url)

doc = BeautifulSoup(response.text, "html.parser")

image = Image.open("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/DF/Main.png")

# 2. 영등포점  ----

## 2-1. 영등포 A Studio ----

### 2-1_1 ) 월수금 ----


elements_table = doc.select("#bin_eng_lesson3 > div > div:nth-child(2) > dl > .time_board > .view_list")

print(len(elements_table))

Def_YDP_MWF_A = []

for element in elements_table:
    Def_YDP_MWF_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDay" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(1)").text ,
        'Time_1': "",
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 3 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

# time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_YDP_MWF_A[0]['Time_1'] = "Afternoon"
Def_YDP_MWF_A[1]['Time_1'] = "Afternoon"
Def_YDP_MWF_A[2]['Time_1'] = "Afternoon"
Def_YDP_MWF_A[3]['Time_1'] = "Night"
Def_YDP_MWF_A[4]['Time_1'] = "Night"
Def_YDP_MWF_A[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_YDP_MWF_A[0]['Genre'] = "Hip-Hop"
Def_YDP_MWF_A[1]['Genre'] = "Girls-HipHop"
Def_YDP_MWF_A[2]['Genre'] = "K-Pop"
Def_YDP_MWF_A[3]['Genre'] = "K-Pop"
Def_YDP_MWF_A[4]['Genre'] = "K-Pop"
Def_YDP_MWF_A[5]['Genre'] = "Hip-Hop"

# print(Def_YDP_MWF_A)

Def_YDP_MWF_A_DF = pd.DataFrame(Def_YDP_MWF_A)

### 2-1_2 ) 화목

elements_table_TT = doc.select("#bin_eng_lesson3 > div > div:nth-child(3) > dl > .time_board > .view_list")
#bin_eng_lesson3 > div > div:nth-child(2) > dl
print(len(elements_table_TT))

Def_YDP_TUETHR_A = []

for element in elements_table_TT:
    Def_YDP_TUETHR_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDay" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(2)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_YDP_TUETHR_A[0]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_A[1]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_A[2]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_A[3]['Time_1'] = "Night"
Def_YDP_TUETHR_A[4]['Time_1'] = "Night"
Def_YDP_TUETHR_A[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_YDP_TUETHR_A[0]['Genre'] = "Hip-Hop"
Def_YDP_TUETHR_A[1]['Genre'] = "Girls-HipHop"
Def_YDP_TUETHR_A[2]['Genre'] = "K-Pop"
Def_YDP_TUETHR_A[3]['Genre'] = "Hip-Hop"
Def_YDP_TUETHR_A[4]['Genre'] = "Girls-HipHop"
Def_YDP_TUETHR_A[5]['Genre'] = "Hip-Hop"

# print(Def_YDP_TUETHR_A)
Def_YDP_TUETHR_A_DF = pd.DataFrame(Def_YDP_TUETHR_A)

### 2-1-3 ) 토일

elements_table_SS = doc.select("#bin_eng_lesson3 > div > div:nth-child(4) > dl > .time_board > .view_list")
print(len(elements_table_SS))

Def_YDP_SS_A = []

for element in elements_table_SS:
    Def_YDP_SS_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "Weekends" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(3)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.


# 2) Genre 수작업
Def_YDP_SS_A[0]['Time_1'] = "Afternoon"
Def_YDP_SS_A[1]['Time_1'] = "Afternoon"
Def_YDP_SS_A[2]['Time_1'] = "Afternoon"
Def_YDP_SS_A[3]['Time_1'] = "Night"
Def_YDP_SS_A[4]['Time_1'] = "Night"

# 1) time 1 수작업
Def_YDP_SS_A[0]['Genre'] = "K-Pop"
Def_YDP_SS_A[1]['Genre'] = "Hip-Hop"
Def_YDP_SS_A[2]['Genre'] = "Breaking"
Def_YDP_SS_A[3]['Genre'] = "K-Pop"
Def_YDP_SS_A[4]['Genre'] = "Girls-HipHop"

# print(Def_YDP_SS_A)
Def_YDP_SS_A_DF = pd.DataFrame(Def_YDP_SS_A)

# ----------------------------------------------------------------
## 2-2. 영등포 B Studio ----

### 2-2_1 ) 월수금 ----

elements_table = doc.select("#bin_eng_lesson3 > div > div:nth-child(5) > dl > .time_board > .view_list")
print(len(elements_table))

Def_YDP_MWF_B = []

for element in elements_table:
    Def_YDP_MWF_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDays" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(4)").text ,
        'Time_1': "",
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 3 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_YDP_MWF_B[1]['Time_1'] = "Afternoon"
Def_YDP_MWF_B[2]['Time_1'] = "Afternoon"
Def_YDP_MWF_B[3]['Time_1'] = "Afternoon"
Def_YDP_MWF_B[4]['Time_1'] = "Night"
Def_YDP_MWF_B[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_YDP_MWF_B[1]['Genre'] = "Girls-HipHop"
Def_YDP_MWF_B[2]['Genre'] = "Hip-Hop"
Def_YDP_MWF_B[3]['Genre'] = "K-Pop"
Def_YDP_MWF_B[4]['Genre'] = "K-Pop"
Def_YDP_MWF_B[5]['Genre'] = "Girls-HipHop"

# print(Def_YDP_MWF_B)
Def_YDP_MWF_B_DF = pd.DataFrame(Def_YDP_MWF_B)


### 2-2_2 ) 화목

elements_table_TT = doc.select("#bin_eng_lesson3 > div > div:nth-child(6) > dl > .time_board > .view_list")
print(len(elements_table_TT))
Def_YDP_TUETHR_B = []

for element in elements_table_TT:
    Def_YDP_TUETHR_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDay" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(5)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_YDP_TUETHR_B[0]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_B[1]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_B[2]['Time_1'] = "Afternoon"
Def_YDP_TUETHR_B[3]['Time_1'] = "Night"
Def_YDP_TUETHR_B[4]['Time_1'] = "Night"

# 2) Genre 수작업
Def_YDP_TUETHR_B[0]['Genre'] = "Girls-HipHop"
Def_YDP_TUETHR_B[1]['Genre'] = "K-Pop"
Def_YDP_TUETHR_B[2]['Genre'] = "K-Pop"
Def_YDP_TUETHR_B[3]['Genre'] = "K-Pop"
Def_YDP_TUETHR_B[4]['Genre'] = "K-Pop"
Def_YDP_TUETHR_B[5]['Genre'] = "Girls-HipHop"

# print(Def_YDP_TUETHR_B)
Def_YDP_TUETHR_B_DF = pd.DataFrame(Def_YDP_TUETHR_B)


### 2-2-3 ) 토일

elements_table_SS = doc.select("#bin_eng_lesson3 > div > div:nth-child(7) > dl > .time_board > .view_list")
print(len(elements_table_SS))

Def_YDP_SS_B = []

for element in elements_table_SS:
    Def_YDP_SS_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "Weekends" ,
        'Day_2': doc.select_one("#bin_eng_lesson3 > div > ul > li:nth-child(6)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_02.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[3] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Yeongdeungpo',
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.


# 2) Genre 수작업
Def_YDP_SS_B[0]['Time_1'] = "Afternoon"
Def_YDP_SS_B[1]['Time_1'] = "Afternoon"
Def_YDP_SS_B[2]['Time_1'] = "Afternoon"
Def_YDP_SS_B[3]['Time_1'] = "Night"
Def_YDP_SS_B[4]['Time_1'] = "Night"

# 1) time 1 수작업
Def_YDP_SS_B[0]['Genre'] = "K-Pop"
Def_YDP_SS_B[1]['Genre'] = "K-Pop"
Def_YDP_SS_B[2]['Genre'] = "Girls-HipHop"
Def_YDP_SS_B[3]['Genre'] = "K-Pop"
Def_YDP_SS_B[4]['Genre'] = "Girls-HipHop"

# print(Def_YDP_SS_B)
Def_YDP_SS_B_DF = pd.DataFrame(Def_YDP_SS_B)


## DF 합치기.

Def_YDP_Total_DF = pd.concat( [ Def_YDP_MWF_A_DF, Def_YDP_TUETHR_A_DF, Def_YDP_SS_A_DF, Def_YDP_MWF_B_DF, Def_YDP_TUETHR_B_DF, Def_YDP_SS_B_DF ], axis = 0)

Def_YDP_Total_DF = Def_YDP_Total_DF.reset_index(drop = True)

# Class_Names 빈 것 지우기
idx_class_none = Def_YDP_Total_DF[Def_YDP_Total_DF['Class_Names'] == ""].index
Def_YDP_Total_DF = Def_YDP_Total_DF.drop(idx_class_none)
# print(Def_YDP_Total_DF)

## csv 파일에 쓰기.: 붙여쓰기 : mode = "a"
Def_YDP_Total_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Def_Dance.csv",
mode = "a", 
encoding="utf-8",
header = False)