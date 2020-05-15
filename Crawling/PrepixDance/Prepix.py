from selenium import webdriver
import pandas as pd
from pandas import DataFrame

# 페이지 이동 및 사이즈 조정
driver = webdriver.Chrome()
driver.get("https://prepixstudio.com/schedule")
driver.set_window_size(3000,3000)

weeks = driver.find_elements_by_css_selector("#app > div > main > div > div > div.item-wrap > div")

print(len(weeks))

# 날짜
#app > div > main > div > div > div.item-wrap > div:nth-child(2) > div.date
Date = weeks[2].find_element_by_css_selector("div.date").text.strip().replace(" ","").split("\n")[0]
Day =  weeks[2].find_element_by_css_selector("div.date").text.strip().replace(" ","").split("\n")[1]
print(Date)
print(Day)

# 수업들 모음 
Classes = weeks[2].find_elements_by_css_selector("div.class")
print(len(Classes))

# time
Classes[0].find_element_by_css_selector("div:nth-child(2)").text

# name
Classes[0].find_element_by_css_selector("div:nth-child(4)").text.split(" ")[0]

Prepix = []


for w in range(0, len(weeks)) :

    Classes = weeks[w].find_elements_by_css_selector("div.class")
    

    if ( w == 0 or w == 6) : # 주말 일때 

        for i in range(0 , len(Classes)) :

            print("%d번째 주 %d번째 class 를 수집중입니다 "  %( w+1, i+1 ) )

            Prepix.append({
                'Academy_Name': 'Prepix Dance' ,
                'Class_Names' : Classes[i].find_element_by_css_selector("div:nth-child(4)").text.split(" ")[0]  ,
                'Day_1' : "Weekends" , 
                'Day_2' : weeks[w].find_element_by_css_selector("div.date").text.strip().replace(" ","").split("\n")[1] ,
                "Time_1" : "Night" ,
                "Time_2" : Classes[i].find_element_by_css_selector("div:nth-child(2)").text ,
                "Genre": "Choreography" ,
                'Link' : "https://prepixstudio.com/schedule" ,
                "Place" : "745 Nonhyun-roh, Gangnam-gu, Seoul",
                "Contact" : "+82 2-518-1470" ,
                "NumOfClass" : "1",
                "District": "Gangnam" ,
                "Img" : "https://prepixstudio.com/images/logo.png"

            })
    else :

        for i in range(0 , len(Classes)) :

            print("%d번째 주 %d번째 class 를 수집중입니다 "  %( w+1, i+1 ) )

            Prepix.append({
                'Academy_Name': 'Prepix Dance' ,
                'Class_Names' : Classes[i].find_element_by_css_selector("div:nth-child(4)").text.split(" ")[0]  ,
                'Day_1' : "WeekDay" , 
                'Day_2' : weeks[w].find_element_by_css_selector("div.date").text.strip().replace(" ","").split("\n")[1] ,
                "Time_1" : "Night" ,
                "Time_2" : Classes[i].find_element_by_css_selector("div:nth-child(2)").text ,
                "Genre": "Choreography" ,
                'Link' : "https://prepixstudio.com/schedule" ,
                "Place" : "745 Nonhyun-roh, Gangnam-gu, Seoul",
                "Contact" : "+82 2-518-1470" ,
                "NumOfClass" : "1",
                "District": "Gangnam" ,
                "Img" : "https://prepixstudio.com/images/logo.png"

            })

Prepix_DF = pd.DataFrame(Prepix)
Prepix_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/PrePix.csv", mode = "w", encoding = "utf-8")


