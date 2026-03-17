import pandas as pd
from collections import defaultdict
import numpy as np

import pandas as pd

df = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8,9,10],
    "name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Helen","Ian","Jack"],
    "dept": ["IT","HR","IT","Finance","HR","IT","Finance","IT","HR","Finance"],
    "salary": [60000,50000,70000,55000,52000,65000,80000,60000,48000,75000],
    "experience": [2,5,7,4,3,6,10,2,1,8],
    "bonus": [5000,4000,None,3000,2000,None,7000,1000,None,5000]
})

'''
#1.Average salary per dept
print(df.groupby('dept')['salary'].mean())

#2.dept_avg_salary using transform
df['dept_avg_salary']=df.groupby('dept')['salary'].transform('mean')

#3.salary_diff = salary - dept_avg_salary
df['salary_diff'] = df['salary'] - df['dept_avg_salary']
print(df)

#4.Get multiple stats per dept: 	avg salary,max salary,avg experience
print(df.groupby('dept').agg({'salary':('mean','max'),'experience':'mean'}))

#5.Same as 4 but use named aggregation
print(df.groupby('dept').agg(
    avg_sal=('salary','mean'),
    max_sal=('salary','max'),
    avg_exp=('experience','mean')
    ))

#6.Group by dept and experience condition:
#Return avg salary only for employees with experience > 3
print(df[df['experience']>3].groupby('dept')['salary'].mean())

#7.Add column: rank inside dept by salary (highest = 1)
df['Salary_Rank']=df.groupby('dept')['salary'].rank(ascending=False,method='first')
print(df)

#8.is_above_dept_avg (True/False)
df['is_above_dept_avg']=df.groupby('dept')['salary'].transform('mean')<df['salary']
print(df)

#9.Remove groups where avg salary < 60000
df=df[df.groupby('dept')['salary'].transform('mean')>60000]
print(df)

#Group by multiple columns:
#dept + experience > 5 flag
#10.Get avg salary. Constraint:must create column first.
df["exp_flag"] = df["experience"] > 5
print(df.groupby(['dept','exp_flag'])['salary'].mean())

'''

#===========================================================
#top 2 salary per dept
print(df.groupby('dept')[['emp_id','name','dept','salary','experience','bonus']]
.apply(lambda x:x.sort_values(by='salary',ascending=False).head(2)))

#Problem 2 — remove dept where max salary < 70000
print(df.groupby('dept').filter(lambda x: x['salary'].max()>70000))

#Problem 3 — keep only highest paid employee per dept
print(df.groupby('dept')[['emp_id','name','dept','salary','experience','bonus']]
.apply(lambda x: x.sort_values('salary',ascending=False).head(1)))

#Problem 4 — groupby + merge pattern (very important)
#Add dept max salary column
dept_max_sal=df.groupby('dept')['salary'].max().reset_index().rename(columns={'salary':'dept_max'})
df=df.merge(dept_max_sal,on='dept',how='left')
print(df)

#Problem 5 — as_index trap
print(df.groupby('dept',as_index=False)['salary'].mean())

#Problem 6 — groupby multiple columns advanced
df['senior']=df["experience"] > 5
print(df.groupby(['dept','senior']).agg(
    avg_sal=('salary','mean'),
    max_bonus=('bonus','max')
    ))

#Problem 7 — NaN behavior in groupby
df.loc[len(df)] = [1, None, None,None,None,None,None,None]
#before
print(df.groupby('dept').sum())
#after
print(df.groupby('dept',dropna=False).sum())

#Problem 8 — groupby sort trap
print(df.groupby('dept',dropna=False,sort=False).sum())


#Problem 9 — performance trap
#Which faster?
#transform
#merge
#apply

#Problem 10 — interview level Get employees whose salary > dept avg
#Constraint:must NOT use transform, Must use:groupby + merge
df=df.merge(df.groupby('dept',as_index=False)['salary'].mean(),on='dept',how='left',suffixes=('','_avg'))
print(df[df['salary']>df['salary_avg']])