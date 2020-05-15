from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/user/Desktop/Web_Study/Dance_Match/Crawling/Justjerk/chromedriver.exe")
# 크롬 드라이버 띄우기
# driver 라는 객체가, 우리가 띄우는 브라우저와 연결되어 있다고 생각하면 된다
# driver 안의 함수를 쓰면, 크롬 브라우저를 컨트롤 할 수 있다.

## 1. 페이지 이동 : get
driver.set_window_size(3000, 3000)

driver.get("http://jerkdemy.com/16")

## 2. 윈도우 사이즈 조절
# driver.set_window_size(3000, 3000)

JestJerkClasses = []

wait = WebDriverWait(driver,10)

## months : 4 weeks 
try:
    months = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mh-plan > tbody > tr")))
    print("성공")
except :
    print("타임아웃")

                                        
## td : 각 주의 day 들
# type(months[1].find_elements_by_css_selector("td"))

## 2번째주 크롤링 
try:
    days = months[1].wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR, "td")))
    print("성공")
except :
    print("타임아웃")
# print(len(days))

try: 
    day = days[1].wait.unitl(EC.element_located_to_be_selected((By.CSS_SELECTOR, "ul > li")))
    print("성공")
except :
    print("타임아웃")
    




