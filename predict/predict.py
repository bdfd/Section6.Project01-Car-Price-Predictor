'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-25 16:43:12
LastEditors  : BDFD
Description  : 
FilePath     : \predict\predict.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template, request
import pandas as pd
import numpy as np
import tempproj as temp
import execdata as exe
predict = Blueprint('predict', __name__,
                    static_folder='static', template_folder='templates')

df = pd.read_csv(
    'https://raw.githubusercontent.com/bdfd/Section6.Project01-Car-Price-Predictor/Pickle-Demo/dataset/Car_Munging_Data.csv',
    encoding='utf-8')
df = df.iloc[:, 1:]
# Check the unique value in company columns
company_lists = df['company'].unique().tolist()
model = temp.Car_Prediction()


@predict.route('/', methods=["POST", "GET"])
def predict_index():
    if request.method == "POST":
        print(company_lists)
        mingzi = request.form["mingzi"]
        name = request.form["name"]
        company = request.form["company"]
        year = request.form["year"]
        year = exe.convint(year)
        kms_driven = request.form["kms_driven"]
        kms_driven = exe.convint(kms_driven)
        fuel_type = request.form["fuel_type"]
        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                data=np.array([name, company, year, kms_driven, fuel_type]).reshape(1, 5)))
        result = str(np.round(prediction[0], 2))
        print(result)
        print(type(mingzi), type(name), type(company),
              type(year), type(kms_driven), type(fuel_type))
        return render_template('homepage/predict_index.html', result=result, name=name, mingzi=mingzi, company=company, year=year, kms_driven=kms_driven, fuel_type=fuel_type)
    else:
        return render_template('homepage/predict_index.html')


# @predict.route('/home')
# def predict_home():
#     return render_template('predict_index.html')
