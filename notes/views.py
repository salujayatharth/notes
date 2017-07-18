from notes import app 
from flask import render_template
from flask import request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submission():

    print (request.form['notes'])
    return render_template('index.html')