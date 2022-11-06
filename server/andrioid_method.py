from flask import Flask, jsonify, request, redirect
from flask_restx import Resource
# python datetime
import datetime 
# 비밀번호 암호화 전용 import
from Crypto.Cipher import AES
from secrets import token_bytes
# db conn import
from database.db import *

# TODO password_encryption class
class Password_encryption:
    # 인코딩
    def encoding(self, user_pw):
        key = token_bytes(16)
        
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(user_pw.encode('ascii'))
        return nonce, ciphertext, tag, key
    
    # 디코딩
    def decoding(self,user_pw1,user_pw2,user_pw3,key):
        cipher = AES.new(key, AES.MODE_EAX, nonce=user_pw1)
        plaintext = cipher.decrypt(user_pw2)
        try:
            cipher.verify(user_pw3)
            return plaintext.decode('ascii')
        except:
            return False
        
#TODO APP user join membership (get, post)
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
        
        # 비밀번호 인코딩
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
        user_grant = "사용자"
        
        vals = (user_id, user_pw1, user_pw2, user_pw3, key, user_name, 
                user_gender, user_email, user_phone, user_date, user_grant)
        cur.execute(sql,vals)
        conn.commit()
# -- header --
# https://203.250.133.144:8080/user-join-membership
# -- body --
# {
# 	"user_id" : "duddjq123",
# 	"user_pw": "wsj5346378~",
# 	"user_name" : "김영업",
#   "user_gender" : "남자",
# 	"user_email": "duddjq123@naver.com",
# 	"user_phone" : "010-6483-2544"
# }

# TODO App user Join (get)
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
# https://203.250.133.144:8080/user-join/dotdotot/wnstjr4428

# TODO App user id find (get)
class user_id_find(Resource):
    def get(self,user_name,user_email,user_phone):
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user_info")
        # all row 가져오기
        res = cur.fetchall()
        
        user_id = ''
        for i in res:
            if (i[5] == user_name and i[7] == user_email and i[8] == user_phone):
                user_id = i[0]
                return jsonify(user_id)
        return 'false'
# https://203.250.133.144:8080/user-id-find/김준석/dotdotot203@naver.com/010-9206-9486

# TODO App user pw find (get)
class user_pw_find(Resource):
    def get(self,user_id,user_name,user_email,user_phone):
        password_encryption = Password_encryption()
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user_info")
        # all row 가져오기
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
# https://203.250.133.144:8080/user-pw-find/dotdotot/김준석/dotdotot203@naver.com/010-9206-9486

# TODO umbrella num check (get)
class manager_create_door_num(Resource):
    def get(self):
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM door")
        # all row 가져오기
        res = cur.fetchall()
        
        num = 0
        # user id 조회
        for i in res:
            num += 1
        return num;
# https://203.250.133.144:8080/manager-create-door-num

# TODO umbrella create (get, post)
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
            main_image.save("C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number + "\\main_image.jpg")
            main_image_path = "C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number
            + "\\main_image.jpg"
        
        second_image_check1 = request.json['second_image_check1']
        more_image1_path = ''
        if(second_image_check1 == "check"):
            second_image1 = request.files['second_image1']
            second_image1.save("C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number + "\\second_image1.jpg")
            more_image1_path = "C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number
            + "\\second_image1.jpg"
        
        second_image_check2 = request.json['second_image_check2']
        more_image2_path = ''
        if(second_image_check2 == "check"):
            second_image2 = request.files['second_image2']
            second_image2.save("C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number + "\\second_image2.jpg")
            more_image2_path = "C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number
            + "\\second_image2.jpg"
        
        second_image_check3 = request.json['second_image_check3']
        more_image3_path = ''
        if(second_image_check3 == "check"):
            second_image3 = request.files['second_image3']
            second_image3.save("C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number + "\\second_image3.jpg")
            more_image3_path = "C:\\vsCode\dream_dream_explan\\server\\save_image\\" + door_number
            + "\\second_image3.jpg"
        
        second_image_check4 = request.json['second_image_check4']
        more_image4_path = ''
        if(second_image_check4 == "check"):
            second_image4 = request.files['second_image4']
            second_image4.save("C:\\vsCode\\server\\dream_dream_explan\save_image\\" + door_number + "\\second_image4.jpg")
            more_image4_path = "C:\\vsCode\\server\\dream_dream_explan\save_image\\" + door_number
            + "\\second_image4.jpg"
        
        # door add
        # MySQL door table values add
        sql = "insert into door values(%s, %s, %s, %s)"

        # door_stats
        door_stats = "판매중"
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

# TODO umbrella delete (delete)
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