import os
import pymysql
from dotenv import load_dotenv
from pathlib import Path

# ✅ Load .env properly
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

class FitnessServices:
    def __init__(self):
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'port': int(os.getenv('DB_PORT')),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }

    def new_register(self, username, email, password, dob, age, gender,  city ):
        flag = False
        con = pymysql.connect(**self.db_config)
        curs = con.cursor()
        qr = f"insert into users (user_name, user_mail, user_pass, dob, age, gender, city) values ('{username}', '{email}', '{password}', '{dob}', {age},'{gender}', '{city}' )"
        curs.execute(qr)
        con.commit()
        curs.close()
        con.close()
        print(str)
        flag=True
        return flag
    
    def authenticate(self, user_mail, user_pass):
        flag = False
        con = pymysql.connect(**self.db_config)
        curs = con.cursor()
        qr = f"Select * from users where user_mail='{user_mail}' and user_pass='{user_pass}'"
        curs.execute(qr)
        data=curs.fetchone()
        if data:
            flag=True
        else:
            flag=False
        curs.close()
        con.close()

        return flag

    
  