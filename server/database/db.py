import pymysql  # mysql 
# mysql setting
conn = pymysql.connect(host='127.0.0.1', user='dotdotot', password='!wnstjr4428', db='my_db', charset='utf8')
# TODO db table property
# # - door table-
# create table door(
# door_number int not null unique,
# door_stats varchar(5) not null,
# registration_date datetime not null,
# primary key(door_number) 
# ); 

# # - door_image table
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

# # - log table -
# create table log_table(
# door_number int not null,
# delete_reason varchar(10) not null,
# delete_date datetime not null,
# registration_date datetime not null,
# user_id varchar(12) not null
# ); 

# # - user_info table -
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