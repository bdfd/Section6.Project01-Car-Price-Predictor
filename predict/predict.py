'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-09 10:48:42
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
company_lists.sort()
name_lists = df['name'].unique().tolist()
name_lists.sort()
year_lists = df['year'].unique().tolist()
year_lists.sort()
fuel_type_lists = df['fuel_type'].unique().tolist()
fuel_type_lists.sort()


@predict.route('/', methods=["POST", "GET"])
def predict_index():
    print(company_lists)
    mingzi = " "
    name = " "
    company = " "
    year = " "
    kms_driven = " "
    fuel_type = " "
    if request.method == "GET":
        return render_template('homepage/predict_index.html', companies=company_lists, car_models=name_lists,
                               year_lists=year_lists, fuel_type_lists=fuel_type_lists,
                               name=name, mingzi=mingzi, company=company, year=year,
                               kms_driven=kms_driven, fuel_type=fuel_type)
    else:
        para_list = []
        mingzi = request.form["mingzi"]
        # para_list.append(mingzi)
        name = request.form["car_models"]
        para_list.append(name)
        company = request.form["company"]
        para_list.append(company)
        year = exe.convint(request.form["year"])
        para_list.append(year)
        kms_driven = exe.convint(request.form["kms_driven"])
        para_list.append(kms_driven)
        fuel_type = request.form["fuel_type"]
        para_list.append(fuel_type)
        # print(para_list)
        result = temp.supervised_classification.Car_Prediction_0601(para_list)
        result = str(np.round(result, 2))
        # print(result)
        return render_template('homepage/predict_index.html', result=result, name=name, mingzi=mingzi,
                               company=company, year=year, kms_driven=kms_driven, fuel_type=fuel_type,
                               companies=company_lists, car_models=name_lists,
                               year_lists=year_lists, fuel_type_lists=fuel_type_lists,
                               )


# @predict.route('/home')
# def predict_home():
#     return render_template('predict_index.html')
