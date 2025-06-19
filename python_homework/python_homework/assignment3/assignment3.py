import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)

#task 1
#create df from dict

data = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age":[25, 30, 35],
    "City":["New York", "Los Angeles", "Chicago"]
}
#convert dict to df
df = pd.DataFrame(data)

#print df
print(df)

#save dr in var task1_task1_data_frame
task1_data_frame = pd.DataFrame(data)

#copy df 
task1_with_salary = task1_data_frame.copy()

#add salary column
task1_with_salary["Salary"] = [70000, 80000, 90000]

#print new df
print(task1_with_salary)

# copy task1 in a var task1 older
task1_older = task1_with_salary.copy()

#increment age by 1
task1_older["Age"] = task1_older["Age"] + 1

#print modified datasheet
print(task1_older)

task1_older.to_csv("employees.csv", index=False)


#task 2

import json


task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

additional_employees = {
    "Name": ["Eve","Frank"], 
    "Age": [28, 40],
    "City": ["Miami", "Seattle"],
    "Salary": [60000, 95000]
}


with open("additional_employees.json", "w") as json_file:
    json.dump(additional_employees, json_file, indent=4)


json_employees = pd.read_json("additional_employees.json")


#combine data from csv and json df to more_employees
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

#print combined data
print(more_employees)


#task 3
#assign first 3 rows of more_employess to var first_three
first_three = more_employees.head(3)
#print var and run test
print(first_three)
#assign last 2 rows of more_employees to var last_two
last_two = more_employees.tail(2)
#print var and run test
print(last_two)
#assign shape of more_employees to var employee_shape
employee_shape = more_employees.shape
#print var and run test
print(employee_shape)
#print summary of df using info()method
print(more_employees.info())

#task 4
#create df from dirty_data.csv and assign to dirty_data
dirty_data = pd.read_csv("dirty_data.csv")
#print and run
print(dirty_data)
#create copy of the dirty data in var clean_data(copy) use data cleaning to update clean_data
clean_data = dirty_data.copy()
#remove dups
clean_data = clean_data.drop_duplicates()
#print and run
print(clean_data)
#convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
#print and run
print(clean_data)
#convert Salary to numeric and replace known pplaceholds with NaN
#clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], np.nan)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
#print and run
print(clean_data)
#fill missing numeric values(fillna) fill Age with mean and salary with median
clean_data["Age"].fillna(clean_data["Age"].mean()),
clean_data["Salary"].fillna(clean_data["Salary"].median())
#print and run
print(clean_data)
#convert hire date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
#print and run
print(clean_data)
#strip xtra wspace and standardize name and dept as upper
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
#print and run
print(clean_data)
