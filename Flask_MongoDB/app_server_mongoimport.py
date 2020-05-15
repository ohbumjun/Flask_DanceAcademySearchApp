# localhost의 sparta > DanceMatch 의 db 를
# Dance 라는 remote DB > Dance > DanceMatch > Dance_Collection으로 옮기는 과정

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId 
# ObjectId str 로 바꿔주기

client = MongoClient('localhost', 27017)
db = client.dbsparta

client_server = MongoClient('mongodb://dhsys112:bjoh1227!!@13.124.200.119', 27017)
db_server = client_server.Dance

app = Flask(__name__)

Classes =list( db.DanceMatch.find({} ,{'_id':0}) )

db_server.Dance_Collection.insert_many(Classes)

db_server.Dance_Collection.count_documents()
