
import mysql.connector
from mysql.connector import errorcode
import hashlib
import sys
import StaticPages
import encryption


# validates login password
def check_password(username, password):
    try:
        cnx = mysql.connector.connect(
        host="45.252.251.80",
        user="gumkgcmv_mialotus",
        password="878787@#Nangong",
        database="gumkgcmv_mialotus"
    )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        if (cnx.is_connected()):
            cursor = cnx.cursor()
            password = password.encode('utf8')
            password = hashlib.sha1(password).hexdigest()
            sql = "SELECT * FROM tbl_account WHERE sUsername = '" + username + "' and sPassword ='"+password+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is None:
                return False
            else:
                return True
        else:
            print("Not connected")
            
