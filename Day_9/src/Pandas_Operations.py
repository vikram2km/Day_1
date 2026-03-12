import pandas as pd
from collections import defaultdict
import numpy as np
'''#Problem 1 — One-to-many validation
employees = pd.DataFrame({
    "emp_id": [1,2,3,4,5],
    "name": ["Alice","Bob","Charlie","David","Eva"],
    "dept_id": [10,20,10,30,20]
})

departments = pd.DataFrame({
    "dept_id": [10,20,30],
    "manager": ["John","Mary","Steve"]
})

#
print(employees.merge(departments,on='dept_id',how='left',validate='many_to_one'))

#Problem 2 — Detect unmatched keys
sales = pd.DataFrame({
    "sale_id": [1,2,3,4],
    "product_id": [100,101,102,999]
})
products = pd.DataFrame({
    "product_id": [100,101,102],
    "name": ["Pen","Book","Bag"]
})
mergee=sales.merge(products,how='left', on='product_id', indicator=True)
print(mergee[mergee['_merge']=='left_only'])

#Problem 3 — Duplicate explosion: many to many not allowed,must raise error
A = pd.DataFrame({
    "id": [1,1],
    "value": ["A","B"]
})

B = pd.DataFrame({
    "id": [1,1,1],
    "code": ["X","Y","Z"]
})

#print(A.merge(B,on='id',how='left',validate="one_to_one"))

#Problem 4 — Multi key + datatype issue
orders = pd.DataFrame({
    "order_id": [1,2],
    "date": ["2024-01-01","2024-01-02"],
    "amount": [100,200]
})

payments = pd.DataFrame({
    "order_id": [1,2],
    "date": pd.to_datetime(["2024-01-01","2024-01-02"]),
    "paid": ["Y","Y"]
})
orders['date']=orders['date'].map(pd.to_datetime)
print(orders.merge(payments,on=['order_id','date'],how='left',indicator=True))


#Problem 5 — Same column names
employees = pd.DataFrame({
    "id": [1,2],
    "salary": [50000,60000]
})

bonus = pd.DataFrame({
    "id": [1,2],
    "salary": [5000,7000]
})

print(employees.merge(bonus, on='id',how='inner',suffixes=['_emp','_bonus']))

#Problem 6 — Find rows only in left
A = pd.DataFrame({
    "id": [1,2,3,4]
})

B = pd.DataFrame({
    "id": [2,3]
})

Merged_Data=A.merge(B, on='id',how='left',indicator=True)
print(Merged_Data[Merged_Data['_merge']=='left_only'])

#Problem 7 — Merge on index
A = pd.DataFrame({
    "name": ["A","B"]
}, index=[1,2])

B = pd.DataFrame({
    "salary": [100,200]
}, index=[1,2])
print(pd.merge(A,B,left_index=True, right_index=True))

#Problem 8 — Performance constraint (no code needed) - If we are merging better to keep uniqe rows and it would be one_to_one
#Problem 9 — ETL pipeline thinking -
merge - pd.merge()
validate - validate=one_to_many
transform - pd.transform()
filter - apply()
export - print()

#Problem 10 — Interview question - many to many and outer join
'''

df = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8],
    "name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Helen"],
    "dept": ["IT","HR","IT","Sales","HR","IT","Finance","IT"],
    "salary": [60000,50000,70000,55000,52000,65000,80000,60000],
    "experience": [2,5,7,4,3,6,10,2],
    "bonus": [5000,4000,None,3000,2000,None,7000,1000]
})

#Problem 1 - increase salary by 10%
df['new_salary']=df['salary']+df['salary']*(0.1)
#print(df)


#Problem 2 - Convert dept to dept_id
map_func=defaultdict(lambda:0,{'IT':1,'HR':2,'Finance':3})
df['dept_id']=df['dept'].map(map_func)
#print(df)

#Problem 3 - apply axis=1 total_pay = salary + bonus only usign apply
def sum_cols_with_nan(row):
    val1 = row['salary'] if pd.notna(row['salary']) else 0
    val2 = row['bonus'] if pd.notna(row['bonus']) else 0
    return val1 + val2
df['total_pay']=df.apply(sum_cols_with_nan,axis=1)
#problem 4: Same as Problem -3 but must use vectorized
df['total_pay']=df[['salary','bonus']].sum(axis=1)
#print(df)

#Problem 5 - dept_avg_salary
df['dept_avg_salary']=df.groupby('dept')['salary'].transform('mean')
#print(df)

#Problem 6 - Must use agg dict style.
print(df.groupby('dept').agg({'salary':['mean','max'],'experience':'mean'}))
print(df.groupby('dept').agg(Avg_Sal=('salary','mean'),
       Max_Sal=('salary','max'),
       Avg_Exp=('experience','mean')))

#===========================Incorrect Approach==============================
def func_2_columns(df):
    df['salary_flag']='High' if df['salary']>65000 else 'Low'
    df['exp_flag']='Senior' if df['experience']>5 else 'Junior'
    return df
print(df.apply(func_2_columns,axis=1))

def fun(row):
    return pd.Series({
        "salary_flag": "High" if row["salary"] > 65000 else "Low",
        "exp_flag": "Senior" if row["experience"] > 5 else "Junior"})
df[['salary_flag','exp_flag']]=df.apply(fun,axis=1)
print(df)
#Problem 8 — transform vs apply confusion
#We can use both but apply is very slow compared to Transform
#and Transform is built mainly for this purpose only. So, Transform should be used for this.

#Problem 9 — NaN behavior
#best method is fillna as it is the built in method to handle Nans

#Problem 10 — performance reasoning
#vectorized
#transform - map comes before Transform
#map
#apply
#apply axis=1

