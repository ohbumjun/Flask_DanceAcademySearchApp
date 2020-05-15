import frzm_google_vision as gtd

# 전략 :
# 증가인덱스 통해서, 각 리스트에 넣을 것이다
# 비어있는 리스트 만들고
# 각 장소에 삽입
frzm_1_HD = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/LP_dance/1_GN.jpg")
print(frzm_1_HD)






# # 우선, 비어있는 리스트 만들기
# frzm_1_HD_list = [0]

# # 요일 제거 
# frzm_1_HD = frzm_1_HD[9:] 

# # 첫주 넣기
# frzm_1_HD_list.insert(0, frzm_1_HD[:15])  

# # 두번째 주 끝 위치 확인
# print(frzm_1_HD.index("유소현"))

# # 둘째주 넣기

# frzm_1_HD_list.insert(1, frzm_1_HD[15:36])  
# print(frzm_1_HD_list[1])

# # 세번째 주 끝 위치 확인
# frzm_1_HD_list.insert(2, frzm_1_HD[36:60])
# print(frzm_1_HD_list[2])

# print(frzm_1_HD.index("김지원")) # 47 : 그 다음 2번째 까지


# # frzm_1_HD_list.insert(3, frzm_1_HD[:15])  

# # # print(frzm_1_HD)
# # print(frzm_1_HD)
# # frzm_2_HD = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/frzm/frzm_2_HD.jpg")
# # print(frzm_2_HD)
# # frzm_3_BP = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/frzm/frzm_3_BP.jpg")
# # print(frzm_3_BP)
# # frzm_4_BP = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/frzm/frzm_4_BP.jpg")
# # print(frzm_4_BP)
# # frzm_5_BP = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/frzm/frzm_5_BP.jpg")
# # print(frzm_5_BP)