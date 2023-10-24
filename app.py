'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-24 18:16:56
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
from predict.predict import predict
import requests
import os
import pandas as pd
import pickle


app = Flask(__name__)

app.register_blueprint(predict, url_prefix="/predict")
df = pd.read_csv(
    'https://raw.githubusercontent.com/bdfd/Section6.Project01-Car-Price-Predictor/Pickle-Demo/dataset/Car_Munging_Data.csv', encoding='utf-8')
df = df.iloc[:, 1:]
model = pickle.load(open('./dataset/LinearRegressionModel.pkl', 'rb'))
# Check the unique value in company columns
company_list = df['company'].unique().tolist()
company_list


@app.route('/')
def index():
    print(company_list)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
