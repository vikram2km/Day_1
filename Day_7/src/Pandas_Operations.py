import pandas as pd
import numpy as np

'''
data = {
    "emp_id": [101,102,103,104,105,106,107,108],
    "department": ["IT","HR","Finance","IT","Sales","HR","IT","Finance"],
    "salary": [60000,45000,70000,52000,48000,65000,60000,55000],
    "experience_years": [3,5,7,2,4,6,8,3]
}

df = pd.DataFrame(data)

#Show employees with salary > 60000
print(df[df['salary']>60000])
#Show employees with experience > 3
print(df[df['experience_years']>3])
#Show IT employees with salary > 50000
print(df.loc[(df['salary']>50000) & (df['department']=='IT'),['salary']])
#Select first 4 rows using iloc
print(df.iloc[0:4])
#only the salary column for employees who work in HR
print(df[df['department']=='HR']['salary'])
#only the salary column for employees who have experience greater than 4 years
print(df[df['experience_years']>=4]['salary'])

#Aggregation
df.groupby('department')['salary'].agg(['mean','max','min','count'])

'''



#=================================================
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 32, 37, 29, 41],
    "salary": [50000, 60000, 70000, 52000, 90000],
    "department": ["HR", "Eng", "Eng", "HR", "Mgmt"]
}

df = pd.DataFrame(data)

#Filter employees age > 30
print(df[df['age']>30])
#Average salary per department
print(df.groupby('department')[['salary']].mean())
#Add new column: salary_band
#Rules: < 55000 → "Low" 55000–75000 → "Medium" 75000 → "High"
condition=[
    (df['salary']<55000),
    (df['salary']>=55000) & (df['salary']<=75000),
    (df['salary']>75000)
    ]
categories=['Low','Medium','High']
df['salary_band']=np.select(condition,categories,default='Unknown')

#Sort by salary descending and take top 3
print(df.sort_values(['salary'],ascending=False).iloc[0:3])
    