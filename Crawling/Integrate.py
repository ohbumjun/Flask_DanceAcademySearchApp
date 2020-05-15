import pandas as pd

## 1. DEF
DF_etc = pd.read_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Def_Dance.csv",  encoding= "utf-8")

## 2. JJ 
JJ = pd.read_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/JJ.csv", encoding = "utf-8")

Yes_Class = JJ[JJ['Class_Names'] == 'DAY OFF'].index

JJ = JJ.drop(Yes_Class)

## 3. We_Flex
We_Flex = pd.read_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/WeFlex_real.csv" ,encoding = 'ISO-8859-1')

## 4. Prepix
Pripix = pd.read_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/PrePix.csv", encoding = "utf-8")

Dance_Total_DF = pd.concat([DF_etc, JJ, We_Flex, Pripix])

Dance_Total_DF = Dance_Total_DF.reset_index(drop = True)

Dance_Total_DF.to_csv("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance_Total.csv", mode = "w", encoding = "utf-8-sig")

