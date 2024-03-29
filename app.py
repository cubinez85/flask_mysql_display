from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
   host="localhost",
   user="cubinez85",
   password="123",
   database="MyDB"
)

cursor = db.cursor()

@app.route('/')
def index():

    cursor.execute("select * from MyUsers")
    output = cursor.fetchall()
    res = str(output).strip('[]')
    
    return res




if __name__ == '__main__':
    app.run()
