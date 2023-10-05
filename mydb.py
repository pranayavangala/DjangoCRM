import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',

)
#prepare the cursor
curserObject = dataBase.cursor()

#create the DataBase

curserObject.execute("CREATE DATABASE crmdb")

print("Data Base ALL DONE!!!")