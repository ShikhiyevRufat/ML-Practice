"""
Create a DataFrame from a dictionary with columns: Name, Age, Salary.
"""

import pandas as pd
import numpy as np

# df = pd.DataFrame({"Name": ['Rufat','Farid','Tural', 'Ruslan'],
#                    "Age": [34, 21, 22,18],
#                    "Salary": [1600, 500, 1000, 700]
#                    })

"""
Convert it into a CSV file.
"""

# df.to_csv('My_data.csv')

"""
Load a CSV file (data.csv) into a DataFrame.
Display the first 5 and last 5 rows.
Get the shape and column names of the DataFrame.
"""
# df = pd.read_csv("My_data.csv")

# df.pop("Unnamed: 0")
# a = df.tail(2)
# print(a)
# df.info()

"""
Select the Age column from the DataFrame.
Filter rows where Age > 30.
Retrieve rows where Salary > 50000 and Age < 35.
"""

# a = df["Age"]
# print(a)
# a = df[df["Age"] > 30]
# print(a)
# a = df[(df["Age"] < 30) & (df["Salary"] > 500)] 
# print(a)

"""
Check for missing values in the dataset.
Fill missing values with the column mean.
Drop rows with any missing values
"""

# b = df.isna() or isnull
# print(b)
# b = df.fillna(df.mean(), inplace=True)
# b = df.dropna()

"""
Sort the DataFrame by Age in ascending order.
Sort by Salary in descending order.
"""

# b = df.sort_values('Age', ascending=False)
# print(b)


"""
Grouping and Aggregation

Group data by Department and find the average salary.
Count the number of employees in each department.
Apply Functions

Create a new column Bonus which is 10% of Salary.
Use apply() to convert all names to uppercase.
Merging and Joining

Create two DataFrames:
One with EmployeeID, Name, Age.
Another with EmployeeID, Department, Salary.
Merge them on EmployeeID.
Pivot Tables

Create a pivot table showing the average salary per department.
Date-Time Handling

Convert a column to datetime format.
Extract the year, month, and day from the date column.
Filter records for a specific month.
"""

# df1 = pd.DataFrame({
#     'EmployeeID': [101, 102, 103, 104, 105],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 40, 45]
# })

# df2 = pd.DataFrame({
#     'EmployeeID': [101, 102, 103, 104, 105],
#     'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
#     'Salary': [50000, 60000, 70000, 80000, 55000]
# })

# df = pd.merge(df1, df2, on="EmployeeID")

# group_salary = df.groupby('Department')['Salary'].mean()
# count_employees = df.groupby('Department')['Name'].count()
# print(count_employees)

# df["Bonus"] = df['Salary'] * 10 // 100

# df['Name'] = df['Name'].apply(lambda x: x.upper())

# pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')

# print(pivot_table)


"""
1. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. 
Set the index to be the first column.
2. Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. 
Fill the DataFrame with random integers and access the element at row 'Y' and column 'B'.
"""

# df = pd.DataFrame(np.random.randint(1,100, size = (6,4)), columns= ['A', 'B', 'C', 'D'])
# print(df)

df = pd.DataFrame(np.random.randint(1,100, size = (3,3)), columns= ['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print(df)

df = pd.DataFrame(np.random.randint(1,100, size = (3,3) ))
