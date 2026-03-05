import pandas as pd
df=pd.DataFrame(
    [['Alice',25,50000],['Bob',30,60000],['Charlie',35,70000]],
columns=['name','age','salary'])

'''
#selecting columns
print(df[['name']])
print(df['name'])

#selecting rows
print(df.iloc[0:2])

#adding new column
df['comapny']=['Genpact','Amazon','Flipcart']
print(df)'''

#average salary by age > 28
print(' Average Salary(age > 28) : ',df[df['age']>28]['salary'].mean())

#==================================================================================
data = {
    "emp_id": [1, 2, 3,4,5],
    "name": ["A", "B", "C",'D','E'],
    "salary": [50000, 60000, 55000,65000,75000]
}
d=pd.DataFrame(data)
print(d[::])
print(d[['salary']])
print(type(d[['salary']]))
