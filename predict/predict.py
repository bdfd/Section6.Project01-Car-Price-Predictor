'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-24 17:17:04
LastEditors  : BDFD
Description  : 
FilePath     : \predict\predict.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template

predict = Blueprint('predict', __name__,
                    static_folder='static', template_folder='templates')


@predict.route('/')
def predict_index():
    return render_template('homepage/home.html')


# @predict.route('/home')
# def predict_home():
#     return render_template('predict_index.html')
