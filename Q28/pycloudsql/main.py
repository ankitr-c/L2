# import datetime
from flask import Flask, jsonify, request, redirect, render_template
import os
import pymysql.cursors
import random
import credentials

conn = pymysql.connect(host=credentials.host,
                             user=credentials.user,
                             password=credentials.password,
                             database=credentials.database)

cursor=conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        id=random.randint(1000,9999)
        name=request.form['name']
        email=request.form['email']
        phno=request.form['phno']
        query="INSERT INTO ppls VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(id,name,email,phno))
        conn.commit()
        return redirect('/')
    else:
        cursor.execute("Select * from ppls")
        all_data=cursor.fetchall()
        return render_template('index.html', all_data=all_data)

@app.route('/delete', methods=['POST'])
def delete_data():
    try:
        id = int(request.form['id'])
        cursor.execute(f"DELETE FROM ppls WHERE id={id}")
        conn.commit()
        return redirect('/')
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    portnumber=int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",debug=True, port=portnumber)
