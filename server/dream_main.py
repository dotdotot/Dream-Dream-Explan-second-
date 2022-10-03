from ast import Pass
from email import message
import json
from flask import Flask, jsonify, request, redirect  # ????? 구현??? ?????? Flask 객체 import
from flask_restx import Api, Resource  # Api 구현??? ?????? Api 객체 import
import pymysql  # mysql 
import datetime # python datetime

# image?? ?????? import
from flask import request
from werkzeug.utils import secure_filename

# logging
import logging
import logging.config

# ??????????? ?????? import
from Crypto.Cipher import AES
from secrets import token_bytes

# mysql setting
conn = pymysql.connect(host='203.250.133.144', user='dotdotot', password='!wnstjr4428', db='my_db', charset='utf8')

# TODO db table property
# # - door ???????? ??????-
# create table door(
# door_number int not null unique,
# door_stats varchar(5) not null,
# registration_date datetime not null,
# umbrella_price int not null,
# primary key(door_number) 
# ); 

# # - door_image ???????? ??????- 
# create table door_image(
# door_number int not null unique,
# main_image_path varchar(50) not null,
# more_image1_path varchar(50),
# more_image2_path varchar(50),
# more_image3_path varchar(50),
# more_image4_path varchar(50),
# foreign key(door_number) references door(door_number) 
# on delete cascade on update cascade;
# );

# # - log ???????? ?????? -
# create table log_table(
# door_number int not null,
# delete_reason varchar(10) not null,
# delete_date datetime not null,
# registration_date datetime not null,
# price int not null,
# sale_user varchar(12) not null
# ); 

# # - user ???????? ?????? -
# create table user_info(
# user_id varchar(12) not null unique,
# user_pw1 varchar(150) not null,
# user_pw2 varchar(150) not null,
# user_pw3 varchar(150) not null,
# user_pw_key varchar(100) not null,
# user_name varchar(4) not null,
# user_gender varchar(2) not null,
# user_email varchar(25),
# user_phone varchar(13) not null,
# user_date datetime not null,
# user_grant varchar(5) not null,
# primary key(user_id)
# ); 

# Flask 객체 ??????, ??????미터?? ??????리????????? ??????????? ???름을 ????????.
app = Flask(__name__) 
# utf8 ?????? (????? 깨짐 방???)
app.config['JSON_AS_ASCII'] = False
# Flask 객체??? Api 객체 ?????
api = Api(app) 

#TODO Arduino ACK,NAK message
class Arduino_Ack_Nak(Resource):
    def post(self, arduinoDoor, arduinoState):
        return {"arduinoDoor" : arduinoDoor, "arduinoState" : arduinoState}
api.add_resource(Arduino_Ack_Nak, "/app-pay-arduino/door/d/<int:arduinoDoor>/<string:arduinoState>")
# -- header --
# https://203.250.133.144:8080/app-pay-arduino/door/d/1/ACK

# TODO Arduino Door Open
class Arduino_Door_Open(Resource):
    def get(self,arduinoDoor):
        return {"arduinoDoor" : arduinoDoor}
# api.add_resource
# -- header --
# https://203.250.133.144:8080/user-join-membership

# TODO password_encryption class
class Password_encryption:
    # ???코딩
    def encoding(self, user_pw):
        # ???????? ??????
        key = token_bytes(16)
        
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(user_pw.encode('ascii'))
        return nonce, ciphertext, tag, key
    
    # ???코딩
    def decoding(self,user_pw1,user_pw2,user_pw3,key):
        cipher = AES.new(key, AES.MODE_EAX, nonce=user_pw1)
        plaintext = cipher.decrypt(user_pw2)
        try:
            cipher.verify(user_pw3)
            return plaintext.decode('ascii')
        except:
            return False

        
#TODO APP user join membership (get, post ??????)
class user_join_membership(Resource):
    def get(self):
        return 'hello'
    def post(self):
        # password_encryption class instance
        password_encryption = Password_encryption()
        
        user_id = request.json['user_id']
        user_pw = request.json['user_pw']
        user_name = request.json['user_name']
        user_gender = request.json['user_gender']
        user_email = request.json['user_email']
        user_phone = request.json['user_phone']
        
        # 비???번호 ???코딩
        user_pw1,user_pw2,user_pw3, key = password_encryption.encoding(user_pw)
        
        # MySQL Server connect
        cur = conn.cursor()
        
        # user add
        # MySQL user_info table values add
        sql = "insert into user_info values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # datetime
        DT = datetime.datetime.today()
        user_date = DT.strftime('%Y/%m/%d %H:%M:%S')
        # user_grant
        user_grant = "?????????"
        
        vals = (user_id, user_pw1, user_pw2, user_pw3, key, user_name, 
                user_gender, user_email, user_phone, user_date, user_grant)
        cur.execute(sql,vals);
        conn.commit()
api.add_resource(user_join_membership, "/user-join-membership")
# -- header --
# https://203.250.133.144:8080/user-join-membership
# -- body --
# {
# 	"user_id" : "duddjq123",
# 	"user_pw": "wsj5346378~",
# 	"user_name" : "????????",
#   "user_gender" : "??????",
# 	"user_email": "duddjq123@naver.com",
# 	"user_phone" : "010-6483-2544"
# }

# TODO App user Join (get ??????)
class user_join(Resource):
    def get(self,userid,userpw):
        password_encryption = Password_encryption()
        
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user_info")
        # all row ??????????
        res = cur.fetchall()
        
        user_grant = ''
        check = False
        # user id 조회
        for i in res:
            if (i[0] == userid):
                # ?????? ???????????? ???????????? 비???번호??? key?? ??????????? ???코딩
                user_pw1 = i[1]
                user_pw2 = i[2]
                user_pw3 = i[3]
                key = i[4]
                user_pw = password_encryption.decoding(user_pw1,user_pw2,user_pw3,key)
                if(user_pw == userpw):
                    user_grant = i[10]
                    check = True
                    break
        if(check):
            return jsonify(user_grant)
        return 'false'
api.add_resource(user_join, "/user-join/<string:userid>/<string:userpw>")    
# -- header --
# https://203.250.133.144:8080/user-join/dotdotot/wnstjr4428

# TODO App user id find (get ??????) 
# -> false?? return?????? 200??????코드 발생?????? 문제
class user_id_find(Resource):
    def get(self,user_name,user_email,user_phone):
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user_info")
        # all row ??????????
        res = cur.fetchall()
        
        user_id = ''
        for i in res:
            if (i[5] == user_name and i[7] == user_email and i[8] == user_phone):
                user_id = i[0]
                return jsonify(user_id)
        return 'false'
api.add_resource(user_id_find, "/user-id-find/<string:user_name>/<string:user_email>/<string:user_phone>")    
# https://203.250.133.144:8080/user-id-find/???????/dotdotot203@naver.com/010-9206-9486

# TODO App user pw find (get ??????)
# -> false?? return?????? 200??????코드 발생?????? 문제 
# -> 비???번호??? ??????????? return값이 true, false?? ?????? ??????코드?? return????? ???결되??? 문제(????? 복잡?????)
class user_pw_find(Resource):
    def get(self,user_id,user_name,user_email,user_phone):
        password_encryption = Password_encryption()
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user_info")
        # all row ??????????
        res = cur.fetchall()
        
        user_pw = ''
        for i in res:
            if (i[0] == user_id and i[5] == user_name and i[7] == user_email and i[8] == user_phone):
                user_pw1 = i[1]
                user_pw2 = i[2]
                user_pw3 = i[3]
                key = i[4]
                user_pw = password_encryption.decoding(user_pw1,user_pw2,user_pw3,key)
                return jsonify(user_pw)
        return 'false'
api.add_resource(user_pw_find, "/user-pw-find/<string:user_id>/<string:user_name>/<string:user_email>/<string:user_phone>")
# https://203.250.133.144:8080/user-pw-find/dotdotot/???????/dotdotot203@naver.com/010-9206-9486

# TODO umbrella num check (get ??????)
# ?????????????? ?????? db??? ???록된 ????????? 개수 return
# ??????로이????????? ????????? 개수?? 몇개????? ??????????????? (2?? 초과금???)
class manager_create_door_num(Resource):
    def get(self):
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM door")
        # all row ??????????
        res = cur.fetchall()
        
        num = 0
        # user id 조회
        for i in res:
            num += 1
        return num;
api.add_resource(manager_create_door_num,"/manager-create-door-num")
# https://203.250.133.144:8080/manager-create-door-num

# TODO umbrella create (get, post ??????)
# ????? ?????? image?? 불러??????것??? ??????????? ??????.
class manager_create_door(Resource):
    def get(self):
        # test
        return "hello"
    def post(self):
        # MySQL Server connect
        cur = conn.cursor()
        
        door_number = request.json['door_number']
        umbrella_price = request.json['umbrella_price']
        
        main_image_check = request.json['main_image_check']
        main_image_path = ''
        if(main_image_check == "check"):
            main_image = request.files['main_image']
            main_image.save("C:\\vsCode\dream_dream_explan\save_image\\" + door_number + "\\main_image.jpg")
            main_image_path = "C:\\vsCode\dream_dream_explan\save_image\\" + door_number
            + "\\main_image.jpg"
        
        second_image_check1 = request.json['second_image_check1']
        more_image1_path = ''
        if(second_image_check1 == "check"):
            second_image1 = request.files['second_image1']
            second_image1.save("C:\\vsCode\dream_dream_explan\save_image\\" + door_number + "\\second_image1.jpg")
            more_image1_path = "C:\\vsCode\dream_dream_explan\save_image\\" + door_number
            + "\\second_image1.jpg"
        
        second_image_check2 = request.json['second_image_check2']
        more_image2_path = ''
        if(second_image_check2 == "check"):
            second_image2 = request.files['second_image2']
            second_image2.save("C:\\vsCode\dream_dream_explan\save_image\\" + door_number + "\\second_image2.jpg")
            more_image2_path = "C:\\vsCode\dream_dream_explan\save_image\\" + door_number
            + "\\second_image2.jpg"
        
        second_image_check3 = request.json['second_image_check3']
        more_image3_path = ''
        if(second_image_check3 == "check"):
            second_image3 = request.files['second_image3']
            second_image3.save("C:\\vsCode\dream_dream_explan\save_image\\" + door_number + "\\second_image3.jpg")
            more_image3_path = "C:\\vsCode\dream_dream_explan\save_image\\" + door_number
            + "\\second_image3.jpg"
        
        second_image_check4 = request.json['second_image_check4']
        more_image4_path = ''
        if(second_image_check4 == "check"):
            second_image4 = request.files['second_image4']
            second_image4.save("C:\\vsCode\dream_dream_explan\save_image\\" + door_number + "\\second_image4.jpg")
            more_image4_path = "C:\\vsCode\dream_dream_explan\save_image\\" + door_number
            + "\\second_image4.jpg"
        
        # door add
        # MySQL door table values add
        sql = "insert into door values(%s, %s, %s, %s)"

        # door_stats
        door_stats = "???매중"
        # registration_date
        DT = datetime.datetime.today()
        registration_date = DT.strftime('%Y/%m/%d %H:%M:%S')
        
        vals = (door_number, door_stats, registration_date, umbrella_price)
        cur.execute(sql,vals)
        
        # door_image add
        # MySQL door_image table values add
        sql = "insert into door_image values(%s, %s, %s, %s, %s, %s)"
        vals = (door_number,main_image_path,more_image1_path,more_image2_path,more_image3_path,more_image4_path)
        cur.execute(sql,vals)
        conn.commit()    
api.add_resource(manager_create_door,"/manager-create-door")      
# -- header --
# https://203.250.133.144:8080/manager-create-door/
# -- body --
# {
# 	"door_number" : 1,
# 	"umbrella_price": 8000,
# 	"main_image_check" : "Nocheck",
#   "main_image" : "1234",
# 	"second_image_check1": "Nocheck",
# 	"second_image1" : "",
#   "second_image_check2" : "Nocheck",
# 	"second_image2": "",
# 	"second_image_check3" : "Nocheck",
#  	"second_image3" : "",
#  	"second_image_check4" : "Nocheck",
#  	"second_image4" : ""
# } 

# TODO umbrella delete (delete ??????)
# door ?????? ??????, door_image cascade?? ?????? ??????, log_table??? 추??? ??????.
class manager_delete_door(Resource):
    def delete(self,door_number,delete_reason,user_id):
        door_number = door_number
        delete_reason = delete_reason
        delete_date = ''
        registration_date = ''
        price = ''
        sale_user = user_id
        
        # MySQL Server connect
        cur = conn.cursor()
        
        # datetime
        DT = datetime.datetime.today()
        delete_date = DT.strftime('%Y/%m/%d %H:%M:%S')
        
        # registration_date, price
        sql = "select * from door where door_number = " + door_number;
        cur.execute(sql)
        res = cur.fetchall()
        print(res)
        for i in res:
            registration_date = i[2]
            price = i[3]
            break
        
        # MySQL log_table table values add
        sql = "insert into log_table values(%s, %s, %s, %s, %s, %s)"
        vals = (door_number, delete_reason, delete_date, registration_date, price, sale_user)
        cur.execute(sql,vals);
        
        # door delete (cascade doot_image to delete)
        sql = "delete from door where door_number = " + door_number
        cur.execute(sql)
        conn.commit()
api.add_resource(manager_delete_door,"/manager-delete-door/<string:door_number>/<string:delete_reason>/<string:user_id>")
# -- header --
# https://203.250.133.144:8080/manager-delete-door/1/?????/dotdotot

# TODO Log(file save)
# 로그 ??????
logger = logging.getLogger()
# 로그??? 출력 기??? ?????? (DEBUG, INFO, WARNING, ERROR, WARNING)
logger.setLevel(logging.INFO)
# log 출력 ??????
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# log?? ????????? 출력
file_handler = logging.FileHandler('C:\\vsCode\dream_dream_explan\\test.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# TODO 로그 출력(cmd??)
@app.before_request
def before_request():
    stream_handler = logging.StreamHandler()
    formatter =logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
# TODO http -> https ?????
@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

# 203.250.133.144:8080 , SSL???증서 ??????
if __name__ == "__main__":
    app.run(debug=True, host='203.250.133.144', port=8080, ssl_context=('C:\\vsCode\dream_dream_explan\ssl\cert.pem', 'C:\\vsCode\dream_dream_explan\ssl\key.pem'))