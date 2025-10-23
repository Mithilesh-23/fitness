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



    def admin_authentication(self, admin_name, admin_pass):
        flag = False
        con = pymysql.connect(**self.db_config)
        curs = con.cursor(pymysql.cursors.DictCursor)
        qr = f"Select * from admin_data where admin_name='{admin_name}' and admin_pass='{admin_pass}'"
        curs.execute(qr)
        curs.close()
        con.close()
        data=curs.fetchone()
        return data
    

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
        curs = con.cursor(pymysql.cursors.DictCursor)
        qr = f"Select * from users where user_mail='{user_mail}' and user_pass='{user_pass}'"
        curs.execute(qr)
        curs.close()
        con.close()
        data=curs.fetchone()
        return data
    

    def select_user(self, user_mail, user_pass):
        flag=False
        con=pymysql.connect(**self.db_config)
        curs=con.cursor()
        qr=f"Select user_name, user_mail, age, gender from users where user_mail='{user_mail}' and user_pass='{user_pass}'"
        curs.execute(qr)
        data = curs.fetchall()
        con.close()
        return data
    
    def user_list(self):
        con=pymysql.connect(**self.db_config)
        curs = con.cursor()
        qr = f'select * from users'
        curs.execute(qr)
        data = curs.fetchall()
        con.close()
        return data
    
    def user_profile_search(self, user_name):
        con=pymysql.connect(**self.db_config)
        curs=con.cursor()
        qr=f"select * from users where user_name='{user_name}'"
        curs.execute(qr)
        data=curs.fetchall()
        print("Search Result:", data)

        con.close()
        curs.close()
        return data
    
    def user_profile_delete(self, user_mail, user_pass):
        con = pymysql.connect(**self.db_config)
        try:
            curs = con.cursor()
            qr = f"DELETE FROM users WHERE user_mail='{user_mail}' and user_pass='{user_pass}'"
            curs.execute(qr)
            con.commit()
            if curs.rowcount > 0:
                return True
            else:
                return False
        finally:
            curs.close()
            con.close()


    def user_profile_modify(self, user_mail, user_pass, height, weight):
        con=pymysql.connect(**self.db_config)
        curs=con.cursor()
        qr=f"update users set height={height}, weight={weight} where user_mail='{user_mail}' and user_pass='{user_pass}'"  
        curs.execute(qr)
        con.commit()
        update_row_qr=f"select * from users where user_mail='{user_mail}' and user_pass='{user_pass}'"
        curs.execute(update_row_qr)
        data=curs.fetchall()
        con.close()
        curs.close()
        return data
  