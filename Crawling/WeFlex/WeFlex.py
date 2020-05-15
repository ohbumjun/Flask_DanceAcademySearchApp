from selenium import webdriver
import pandas as pd
from pandas import DataFrame

# 페이지 이동 및 사이즈 조정
driver = webdriver.Chrome()
driver.get("https://wedanceseoul.com/aprill")
driver.set_window_size(3000,3000)

weeks = driver.find_elements_by_css_selector(".row > .col:not(:first-child)")

We_Flex = []

# print(weeks)

# 5개 요일. 각각 5개 수업 ( 리스트 안에 리스트가 들어있는 형태)
for week in weeks:
    for i in range(0,5):
        We_Flex.append({
            'Academy_Name': 'WeFlex' ,
            'Class_Names' : " ".join(week.find_element_by_css_selector(".sqs-block:nth-child({}) > .sqs-block-content".format(i+3)).text.split(" ")[1:]) ,
            'Day_1' : "WeekDay" , 
            'Day_2' : week.find_element_by_css_selector(".sqs-block:nth-child(2) > .sqs-block-content").text ,
            "Time_1" : "Night" ,
            "Time_2" : week.find_element_by_css_selector(".sqs-block:nth-child({}) > .sqs-block-content".format(i+3)).text.split(" ")[0] ,
            "Genre": "" ,
            'Link' : "https://wedanceseoul.com/aprill" ,
            "Place" : "2f, 19, World Cup Buk-ro, Mapo-gu, Seoul, Republic of Korea",
            "Contact" : "+82 2 324 7786" ,
            "NumOfClass" : "",
            "District": "Mapo" ,
            "Img" : "https://static1.squarespace.com/static/58bd1622bf629aed77ceee4b/t/5e6f4a698afded74f569f614/1586945438172/?format=1500w"

        })

We_Flex_DF = pd.DataFrame(We_Flex)
We_Flex_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Weflex_real.csv", mode = "w", encoding = "utf-8")






