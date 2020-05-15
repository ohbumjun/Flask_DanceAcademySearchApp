from pymongo import MongoClient
import csv

# DB connectivity
client = MongoClient('localhost', 27017)
# dbsparta 라는 곳에 넣는다
dbsparta = client.dbsparta 
collection = dbsparta.collection 

# Function to parse csv to dictionary
def csv_to_dict():
    reader = csv.DictReader(open("C:/Users/user/Desktop/Web_Study/Dance_Match/Dance_Total.csv"))
    result = {}
    for row in reader:
        key = row.pop('Academy_Name')
        result[key] = row

    return result

# Final insert statement
dbsparta.DanceMatch.insert_one(csv_to_dict())