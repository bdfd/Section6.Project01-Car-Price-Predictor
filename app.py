'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-20 13:48:05
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from predict.predict import prediction
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.register_blueprint(prediction, url_prefix="/predict")


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
