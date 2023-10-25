'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-25 15:07:28
LastEditors  : BDFD
Description  : 
FilePath     : \predict\predict.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template
import pandas as pd
import numpy as np
import tempproj as temp

predict = Blueprint('predict', __name__,
                    static_folder='static', template_folder='templates')

df = pd.read_csv(
    'https://raw.githubusercontent.com/bdfd/Section6.Project01-Car-Price-Predictor/Pickle-Demo/dataset/Car_Munging_Data.csv',
    encoding='utf-8')
df = df.iloc[:, 1:]
# Check the unique value in company columns
company_lists = df['company'].unique().tolist()
model = temp.Car_Prediction()


@predict.route('/')
def predict_index():
    print(company_lists)
    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'], 
                                            data=np.array(['Maruti Suzuki Swift', 'Maruti', 2019, 100, 'Petrol']).reshape(1, 5)))
    result = str(np.round(prediction[0], 2))
    print(result)
    return render_template('homepage/predict_index.html')


# @predict.route('/home')
# def predict_home():
#     return render_template('predict_index.html')
