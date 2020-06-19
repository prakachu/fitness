from flask import Flask, render_template, url_for, request,session, redirect,make_response, jsonify,flash, Response,send_from_directory
from pymongo import MongoClient


# Define the mongoclient for crud applications
client = MongoClient()
#create a test instance
db = client.test_database

#create a flask based instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/joinTrainer")
def joinTrainer():
    return render_template("join.html")

@app.route("/joinUser")
def joinUser():
    return render_template("joinUser.html")

@app.route("/addTrainer",methods=['POST','GET'])
def addTrainer():
    data = request.form
    user={}
    for i in data:
        user[i]= data[i]
    user['activity']=request.form.getlist('activity')
    users = db.users
    users.insert_one(user)
    return redirect(url_for('index'))

@app.route("/addUser",methods=['POST','GET'])
def addUser():
    data = request.form
    user={}
    for i in data:
        user[i]= data[i]
    user['activity']=request.form.getlist('activity')
    users = db.users
    users.insert_one(user)
    return redirect(url_for('index'))

@app.route("/programs")
def programs():
    return render_template('programs.html')

@app.route('/trainers')
def trainers():
    return render_template('trainer.html')

@app.route('/allServices')
def allServices():
    return render_template("index.html")

app.secret_key = 'mysecret'
if __name__ == "__main__":
	#app.run(host='0.0.0.0',port = '80',debug=True)
	app.run(debug=True)

