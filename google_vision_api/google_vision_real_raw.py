import google_text_detection as gtd

# ()안에, local 내에 text 를 뽑고 싶은 이미지를 넣자
ret = gtd.detect_text("C:/Users/user/Desktop/Web_Study/Dance_Match/Image/frzm/frzm_1_HD.jpg")
print(ret)