import pandas as pd

data = {
    "name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace"],
    "department": ["HR","IT","IT","Finance","HR","IT","Finance"],
    "salary": [50000,60000,70000,65000,60000,55000,80000],
    "experience_years": [2,4,6,5,3,2,8]
}

df = pd.DataFrame(data)


#Write code to return names of employees whose salary is greater than 65000.
print(df.loc[df['salary']>65000,'name'])
#Return a DataFrame containing employees who: work in IT, have experience greater than 3
print(df.loc[(df['department']=='IT')&(df['experience_years']>3)])
#Write code to sort employees by salary descending.
print(df.sort_values('salary',ascending=False))
#Calculate the average salary for each department
print(df.groupby('department')['salary'].mean())
'''Write code to return:

IT         3
HR         2
Finance    2'''
print(df.groupby('department')['department'].value_counts())

#Count how many employees belong to each department using value_counts()
print(df['department'].value_counts())
#Show the top 2 highest salaries using nlargest()
print(df.nlargest(2,'salary'))
#Sort the dataframe by:department salary descending
print(df.sort_values(['department','salary'],ascending=[True,False]))
#Create a column called: dept_avg_salary using Transform
df['dept_avg_salary']=df.groupby('department')['salary'].transform('mean')
print(df)
#Show employees whose salary is greater than department average.
print(df[df['salary']>df['dept_avg_salary']])



employees = pd.DataFrame({
    'emp_id':[1,2,3,4,5,6],
    'name':['Alice','Bob','Charlie','David','Eva','Frank'],
    'department':['IT','HR','IT','Finance','HR','IT'],
    'salary':[60000,50000,70000,55000,52000,65000]
})

departments = pd.DataFrame({
    'department':['IT','HR','Finance'],
    'manager':['John','Mary','Steve']
})

#Join employees with department manager.
employees.merge(departments, on='department', how='left')
#Create duplicate row first:  remove duplicates.
employees2 = pd.concat([employees, employees])
employees2.drop_duplicates('emp_id')

#We want ranking per department.
employees['salary_rank']=employees.groupby('department')['salary'].rank(ascending=False,method='first')
print(employees)

#We want average salary per department.
print(pd.pivot_table(employees,values='salary',index='department',aggfunc='mean'))

#Show employees who earn more than department average only with todays concepts
df=pd.pivot_table(employees,values='salary',index='department',aggfunc='mean').reset_index().rename(columns={'salary':'avg_salary'})
employees=employees.merge(df,on='department',how='left')
print(employees[employees['salary']>employees['avg_salary']])