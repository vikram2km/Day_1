import pandas as pd

df = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8,9,10],
    "name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Helen","Ian","Jack"],
    "dept": ["IT","HR","IT","Finance","HR","IT","Finance","IT","HR","Finance"],
    "salary": [60000,50000,70000,55000,None,65000,80000,60000,48000,75000],
    "experience": [2,5,7,4,3,6,10,2,1,8],
    "bonus": [5000,4000,None,3000,2000,None,7000,1000,None,5000],
    "join_date": [
        "2022-01-15","2021-06-10","2021-03-20","2019-07-01","2023-02-11",
        "2021-09-23","2017-11-30","2022-12-05","2023-08-19","2016-04-14"
    ]
})


#Department's Aevrage Salary
print(df.pivot_table(index='dept',values='salary',aggfunc='mean'))

#Get:dept → avg salary + max salary
print(df.pivot_table(index='dept',values='salary',aggfunc=['mean','max']))

#rows → dept  
#columns → experience > 5 (True/False)  
#values → avg salary
df['Emp_GT_5']=df["experience"]>5
print(df.pivot_table(index='dept',columns='Emp_GT_5',values='salary',aggfunc='mean'))

#Same as Problem 3 Constraint:
#fill missing with 0 and use pivot_table parameter
print(df.pivot_table(index='dept',columns='Emp_GT_5',values='salary',aggfunc='mean',fill_value=0))

#Problem 5 — margins (total row)
print(df.pivot_table(index='dept',columns='Emp_GT_5',values='salary',aggfunc='mean',fill_value=0,margins=True))



#PART 2 — Missing Values (NaN Deep Dive)

#Problem 6 — count missing values per column
print(df.isnull().sum())

#Problem 7 — fill only bonus column with 0
df['bonus']=df['bonus'].fillna(0)
print(df)

#Problem 8 — drop rows where salary is missing
df=df.dropna(subset='salary')
print(df)

#Problem 9 — forward fill (ffill)
#Sort by join_date, then fill missing bonus using previous value.
df=df.sort_values(by=['join_date'])
df['bonus']=df['bonus'].ffill()

#PART 3 — String Operations
#Problem 10 — string cleaning
#Create column: name_upper → uppercase names
df['name_upper']=df['name'].str.upper()
print(df)

#Problem 11 — filter names containing 'a'
print("Names containing a \n",df.query("name.str.contains('a')"))

#PART 4 — Datetime
#join_date → datetime
df['join_date']=pd.to_datetime(df['join_date'])

#Problem 12 — extract year
df['join_year']=df['join_date'].dt.year

#Problem 13 — experience from date, Use current year approx (2026)
df['experience']=2026-df['join_year']

#Problem 14 — filter recent employees
#Employees who joined after 2021
print(df[df['join_year']>2021])

#Problem 15
#dept-wise avg salary of employees who:
#- joined after 2020
#- have bonus missing
pq=df.query('join_year>2020 and bonus.isnull()').groupby('dept')['salary'].mean()
print(pq)