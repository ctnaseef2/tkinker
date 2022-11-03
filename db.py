import mysql.connector
def connect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="video_app_db"
    )
    return mydb
def insert_data(username,password):
    db=connect()
    mycursor = db.cursor()

    sql = "INSERT INTO video_app (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)

    db.commit()
    print(mycursor.rowcount, "record inserted.")
    if mycursor.rowcount > 0:
        return True
    return False
def search_data(username,password):
    mydb=connect()
    mycursor = mydb.cursor()
    sql = "SELECT username, password FROM video_app WHERE username=%s COLLATE utf8mb4_0900_as_cs  AND password = %s COLLATE utf8mb4_0900_as_cs  "
    adr = (username,password)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchone()
    print(myresult)
    if myresult:
        return True
    return False
def validate_data(username):
    mydb=connect()
    mycursor = mydb.cursor()
    sql = "SELECT username, password FROM video_app WHERE username=%s COLLATE utf8mb4_0900_as_cs"
    adr = (username,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchone()
    print(myresult)
    if myresult:
        return False
    return True
