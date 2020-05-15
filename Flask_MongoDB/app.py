
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId 
# ObjectId str 로 바꿔주기


client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index_dance.html')


@app.route('/class', methods= ['GET'] )
def read_reviews():


    # Genre_receive로 클라이언트가 준 Genre 가져오기
    Genre_receive = request.args.get('Genre_give');
    # Day_receive로 클라이언트가 준 Day 가져오기
    Day_receive = request.args.get('Day_give');
    # Time_receive로 클라이언트가 준 Time 가져오기
    Time_receive = request.args.get('Time_give');
    # District+receive로 칼리언트가 준 District 가져오기
    District_receive = request.args.get('District_give');

    Classes = list( db.DanceMatch.find( { 'Genre' : Genre_receive , 'Day_1' : Day_receive  ,  'Time_1' : Time_receive, 
    'District' : District_receive } , {'_id':0}) )

    

    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'Classes': Classes})



if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
    #  app.run('0.0.0.0', port=5000, debug=True)
    
# local 로 돌릴 때는 아래로 해라 