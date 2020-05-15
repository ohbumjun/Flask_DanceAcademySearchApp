import requests
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# from PIL import Image

# DB 세팅
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


# 공통 코드
url = "https://www.defcompany.com/defdance/sub_dance_01_01.html"

response = requests.get(url)

doc = BeautifulSoup(response.text, "html.parser")

# image = Image.open("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/DF/Main.png")

# 1. 강남점  ----

## 1-1. 강남 A Studio ----

### 1-1_1 ) 월수금 ----

elements_table = doc.select("#bin_eng_lesson2 > div > div:nth-child(2) > dl > .time_board > .view_list")
print(len(elements_table))

Def_GangNam_MWF_A = []

for element in elements_table:
    Def_GangNam_MWF_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDay" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:first-child").text ,
        'Time_1': "",
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 3 ,
        'District' : 'Gangnam' ,
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_GangNam_MWF_A[0]['Time_1'] = "Afternoon"
Def_GangNam_MWF_A[1]['Time_1'] = "Afternoon"
Def_GangNam_MWF_A[2]['Time_1'] = "Afternoon"
Def_GangNam_MWF_A[3]['Time_1'] = "Night"
Def_GangNam_MWF_A[4]['Time_1'] = "Night"
Def_GangNam_MWF_A[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_GangNam_MWF_A[0]['Genre'] = "Hip-Hop"
Def_GangNam_MWF_A[1]['Genre'] = "K-Pop"
Def_GangNam_MWF_A[2]['Genre'] = "Hip-Hop"
Def_GangNam_MWF_A[3]['Genre'] = "K-Pop"
Def_GangNam_MWF_A[4]['Genre'] = "K-Pop"
Def_GangNam_MWF_A[5]['Genre'] = "Hip-Hop"


# print(type(Def_GangNam_Datas))
# print(Def_GangNam_MWF_A)

Def_GangNam_MWF_A_DF = pd.DataFrame(Def_GangNam_MWF_A)

# Def_GangNam_MWF_A_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")



## 1-1_2 ) 화목

elements_table_TT = doc.select("#bin_eng_lesson2 > div > div:nth-child(3) > dl > .time_board > .view_list")
print(len(elements_table_TT))

Def_GangNam_TUETHR_A = []

for element in elements_table_TT:
    Def_GangNam_TUETHR_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "Weekday" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:nth-child(2)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Gangnam' ,
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_GangNam_TUETHR_A[0]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_A[1]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_A[2]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_A[3]['Time_1'] = "Night"
Def_GangNam_TUETHR_A[4]['Time_1'] = "Night"
Def_GangNam_TUETHR_A[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_GangNam_TUETHR_A[0]['Genre'] = "Hip-Hop"
Def_GangNam_TUETHR_A[1]['Genre'] = "K-Pop"
Def_GangNam_TUETHR_A[2]['Genre'] = "Girls-HipHop"
Def_GangNam_TUETHR_A[3]['Genre'] = "Hip-Hop"
Def_GangNam_TUETHR_A[4]['Genre'] = "Girls-HipHop"
Def_GangNam_TUETHR_A[5]['Genre'] = "Hip-Hop"


Def_GangNam_TUETHR_A_DF = pd.DataFrame(Def_GangNam_TUETHR_A)
# print(Def_GangNam_DF_TURTHR.tail(2))
# Def_GangNam_TUETHR_A_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")


### 1-1-3 ) 토일

elements_table_SS = doc.select("#bin_eng_lesson2 > div > div:nth-child(4) > dl > .time_board > .view_list")
print(len(elements_table_SS))

Def_GangNam_SS_A = []

for element in elements_table_SS:
    Def_GangNam_SS_A.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "Weekends" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:nth-child(3)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : 'Gangnam' ,
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.


# 2) Genre 수작업
Def_GangNam_SS_A[0]['Time_1'] = "Afternoon"
Def_GangNam_SS_A[1]['Time_1'] = "Afternoon"
Def_GangNam_SS_A[2]['Time_1'] = "Afternoon"
Def_GangNam_SS_A[3]['Time_1'] = "Night"
Def_GangNam_SS_A[4]['Time_1'] = "Night"

# 1) time 1 수작업
Def_GangNam_SS_A[0]['Genre'] = "K-Pop"
Def_GangNam_SS_A[1]['Genre'] = "Hip-Hop"
Def_GangNam_SS_A[2]['Genre'] = "Hip-Pop"
Def_GangNam_SS_A[3]['Genre'] = "K-Pop"
Def_GangNam_SS_A[4]['Genre'] = "Hip-Hop"

# print(type(Def_GangNam_Datas))
# print(Def_GangNam_SS_A)

Def_GangNam_SS_A_DF = pd.DataFrame(Def_GangNam_SS_A)
# print(Def_GangNam_DF_SS.tail(2))
# Def_GangNam_SS_A_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")

# --------------------------------------------------------
# 1-2. 강남 B Studio ----

### 1-2_1 ) 월수금 ----

elements_table = doc.select("#bin_eng_lesson2 > div > div:nth-child(5) > dl > .time_board > .view_list")
print(len(elements_table))

Def_GangNam_MWF_B = []

for element in elements_table:
    Def_GangNam_MWF_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDays" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:first-child").text ,
        'Time_1': "",
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 3 ,
        'District' : "Gangnam",
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_GangNam_MWF_B[0]['Time_1'] = "Afternoon"
Def_GangNam_MWF_B[1]['Time_1'] = "Afternoon"
Def_GangNam_MWF_B[2]['Time_1'] = "Afternoon"
Def_GangNam_MWF_B[3]['Time_1'] = "Night"
Def_GangNam_MWF_B[4]['Time_1'] = "Night"
Def_GangNam_MWF_B[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_GangNam_MWF_B[0]['Genre'] = "Hip-Hop"
Def_GangNam_MWF_B[1]['Genre'] = "Girls-HipHop"
Def_GangNam_MWF_B[2]['Genre'] = "K-Pop"
Def_GangNam_MWF_B[3]['Genre'] = "K-Pop"
Def_GangNam_MWF_B[4]['Genre'] = "Girls-HipHop"
Def_GangNam_MWF_B[5]['Genre'] = "Girls-HipHop"


# print(type(Def_GangNam_Datas))
# print(Def_GangNam_MWF_B)

Def_GangNam_MWF_B_DF = pd.DataFrame(Def_GangNam_MWF_B)
# print(Def_GangNam_DF_B.tail(2))
# Def_GangNam_MWF_B_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")


### 1-2_2 ) 화목

elements_table_TT = doc.select("#bin_eng_lesson2 > div > div:nth-child(6) > dl > .time_board > .view_list")
print(len(elements_table_TT))

Def_GangNam_TUETHR_B = []

for element in elements_table_TT:
    Def_GangNam_TUETHR_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "WeekDay" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:nth-child(2)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        'District' : "Gangnam",
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.

# 1) time 1 수작업
Def_GangNam_TUETHR_B[0]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_B[1]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_B[2]['Time_1'] = "Afternoon"
Def_GangNam_TUETHR_B[3]['Time_1'] = "Night"
Def_GangNam_TUETHR_B[4]['Time_1'] = "Night"
Def_GangNam_TUETHR_B[5]['Time_1'] = "Night"

# 2) Genre 수작업
Def_GangNam_TUETHR_B[0]['Genre'] = "Hip-Hop"
Def_GangNam_TUETHR_B[1]['Genre'] = "Girls-HipHop"
Def_GangNam_TUETHR_B[2]['Genre'] = "Girls-HipHop"
Def_GangNam_TUETHR_B[3]['Genre'] = "K-Pop"
Def_GangNam_TUETHR_B[4]['Genre'] = "K-Pop"
Def_GangNam_TUETHR_B[5]['Genre'] = "Hip-Hop"


# print(type(Def_GangNam_Datas))
# print(Def_GangNam_TUETHR_B)

Def_GangNam_TUETHR_B_DF = pd.DataFrame(Def_GangNam_TUETHR_B)
# print(Def_GangNam_DF_TURTHR.tail(2))
# Def_GangNam_TUETHR_B_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")


### 1-2-3 ) 토일

elements_table_SS = doc.select("#bin_eng_lesson2 > div > div:nth-child(7) > dl > .time_board > .view_list")
print(len(elements_table_SS))

Def_GangNam_SS_B = []

for element in elements_table_SS:
    Def_GangNam_SS_B.append({
        'Academy_Name': 'Def_Dance' ,
        'Class_Names': element.select_one(".view_02 > center > font").text ,
        'Day_1': "Weekends" ,
        'Day_2': doc.select_one("#bin_eng_lesson2 > div > ul > li:nth-child(3)").text , 
        'Time_1': "" ,
        'Time_2': element.select_one(".view_01").text ,
        'Genre': "" ,
        'Link': "https://www.defcompany.com/defdance/sub_dance_01_01.html" ,
        'Place': doc.select_one("#footer_container > div.com_information > div.address1").text.split("\n")[2] ,
        'Contact': doc.select_one("#timeboard_eng_tittle > div.view").text.split("\n")[0] ,
        'NumOfClass': 2 ,
        "District": "Gangnam" ,
        "Img" : "https://www.defcompany.com/defdance/left_banner/def-menu-top2019.png"
    })

## time 1 과 Genre 는 수작업이 들어가야 한다.


# 2) Genre 수작업
Def_GangNam_SS_B[0]['Time_1'] = "Afternoon"
Def_GangNam_SS_B[1]['Time_1'] = "Afternoon"
Def_GangNam_SS_B[2]['Time_1'] = "Afternoon"
Def_GangNam_SS_B[3]['Time_1'] = "Night"
Def_GangNam_SS_B[4]['Time_1'] = "Night"

# 1) time 1 수작업
Def_GangNam_SS_B[0]['Genre'] = "K-Pop"
Def_GangNam_SS_B[1]['Genre'] = "Hip-Hop"
Def_GangNam_SS_B[2]['Genre'] = "Girls-HipHop"
Def_GangNam_SS_B[3]['Genre'] = "Girls-HipHop"
Def_GangNam_SS_B[4]['Genre'] = "Breaking"


Def_GangNam_SS_B_DF = pd.DataFrame(Def_GangNam_SS_B)
# print(Def_GangNam_DF_SS_B.tail(2))

# Def_GangNam_SS_B_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance.csv", encoding="utf-8-sig")

## DF 합치기.

Def_GangNam_Total_DF = pd.concat( [ Def_GangNam_MWF_A_DF, Def_GangNam_TUETHR_A_DF, Def_GangNam_SS_A_DF, Def_GangNam_MWF_B_DF, Def_GangNam_TUETHR_B_DF, Def_GangNam_SS_B_DF ], axis = 0)

Def_GangNam_Total_DF = Def_GangNam_Total_DF.reset_index(drop = True)

# class_name 없는 거 지우기 

idx_class_none = Def_GangNam_Total_DF[Def_GangNam_Total_DF['Class_Names'] == ""].index
Def_GangNam_Total_DF = Def_GangNam_Total_DF.drop(idx_class_none)

# print(Def_GangNam_Total_DF)

## csv 파일에 쓰기.
Def_GangNam_Total_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Def_Dance.csv",mode = "w", encoding="utf-8")
# default : header = True >> 열 이름을 붙이게 된다 