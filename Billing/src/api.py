from src import app
from flask import request
import json
import mysql.connector


mydb = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="catty",
    database="billdb"
)

mycursor = mydb.cursor()

@app.route("/health")
def index():
    return "OK"

@app.route('/provider',methods=['POST'])
def Insert_provider():
    sql = "INSERT INTO Provider (id,name) VALUES (%s,%s)"
    val = ('9',request.form['name'])
    mycursor.execute(sql, val)

    mydb.commit()

    return "record inserted"