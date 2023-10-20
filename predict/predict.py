'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-20 13:44:52
LastEditors  : BDFD
Description  : 
FilePath     : \prediction\prediction.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template

prediction = Blueprint('prediction', __name__,
                       static_folder='static', template_folder='templates')


@prediction.route('/home')
@prediction.route('/')
def home():
    return render_template('home.html')
