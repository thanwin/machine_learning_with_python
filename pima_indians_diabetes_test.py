#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:04:49 2018

@author: ict
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#https://gist.github.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f
# 1. Pregnancies :: Number of times pregnant
# 2. Glucose :: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. BloodPressure :: Diastolic blood pressure (mm Hg)
# 4. SkinThickness :: Triceps skin fold thickness (mm)
# 5. Insulin :: 2-Hour serum insulin (mu U/ml)
# 6. BMI :: Body mass index (weight in kg/(height in m)^2)
# 7. Pedigree :: Diabetes pedigree function
# 8. Age :: Age (years)
# 9. Class variable (0 or 1)
#url for the pima_indians_diabetes dataset in csv
file_url = 'https://gist.githubusercontent.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f/raw/819b69b5736821ccee93d05b51de0510bea00294/pima-indians-diabetes.csv'
#column names for df
df_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Pedigree', 'Age', 'Outcome']
#read csv from url 
df = pd.read_csv(file_url, header=0, skiprows=9, names=df_names)
#view dimension 
print(df.shape)
#view first 20 rows
print(df.head(20))
#veiw summary of the dataset
print(df.describe())

#view correlation
sns.pairplot(df, hue="Outcome")

#table name for the dataset
db_table = 'tbl_pima_indians_diabetes'
#create engine for postgresql database
engine = create_engine('postgresql://postgres:postgres@192.168.122.170/mldb', echo=True)
#save the dataframe into postgresql database
df.to_sql(db_table, engine)
