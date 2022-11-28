from flask import Flask, jsonify, request, redirect  
from flask_restx import Api, Resource 

from andrioid_method import *;
from arduino_method import *; 
from log.log import *;

# Flask 객체 
app = Flask(__name__) 
# utf8 글자 깨짐 방지
app.config['JSON_AS_ASCII'] = False

# TODO http -> https 변환해서 접속
@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

api = Api(app) 

# android method attach
api.add_resource(user_join_membership, "/user-join-membership")    
api.add_resource(user_join, "/user-join/<string:userid>/<string:userpw>")   
api.add_resource(user_info, "/user-info/<string:user_id>/<string:user_pw>")   
api.add_resource(user_id_find, "/user-id-find/<string:user_name>/<string:user_email>/<string:user_phone>")   
api.add_resource(user_pw_find, "/user-pw-find/<string:user_id>/<string:user_name>/<string:user_email>/<string:user_phone>")   
api.add_resource(manager_rental_door, "/manager-rental-door/<string:door_number>")
api.add_resource(manager_return_door, "/manager-return-door/<string:door_number>")
api.add_resource(manager_rental_check, "/manager-rental-check/<int:door_number>")
api.add_resource(manager_create_door_num, "/manager-create-door-num")   
api.add_resource(manager_create_door, "/manager-create-door")   
api.add_resource(manager_delete_door, "/manager-delete-door/<int:door_number>/<string:delete_reason>/<string:user_id>")   
# arduino method attach

# 203.250.133.144:8080 , SSL 인증서 부착
if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.32', port=8080, ssl_context=('C:\\vsCode\dream_dream_explan\\server\\ssl\cert.pem', 'C:\\vsCode\dream_dream_explan\\server\\ssl\key.pem'))
