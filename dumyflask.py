# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:11:37 2019

@author: Winchester
"""
import flask
#import request
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def start():
    return "print hello"

@app.route("/get")
def get_bot_response():
    return "getting response"

@app.route("/postm",methods=('GET','POST'))
def post_message():
    method_req = request.method
    print('form: ',request.form,request.data)
    return "getting response via {}".format(method_req)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)