#task 2 
import csv


def read_employees():
    info = {}
    rows = []
    try:
        with open('../csv/employees.csv' , 'r') as file:
           csv_reader = csv.reader(file)

           for index, row in enumerate(csv_reader):
               if index == 0:
                   info["fields"] = row
               else:  
                   rows.append(row) 

        info["rows"] = rows
        return info
    except Exception as e:
        print(f"An error occured: {e}")
        exit()
      
employees = read_employees()
print(employees)

#task 3

def column_index(first_name):
    return employees["fields"].index(first_name)

employee_id_column = column_index("employee_id")
print(f"Indx of 'employee_id' column: {employee_id_column}")


#task 4
 
def first_name(row_num):

    first_name_index = column_index('first_name')
    return employees["rows"][row_num][first_name_index]
    print(first_name(0))


#task 5

def employee_find(employee_id):
    def employee_match(row): 
        try:   
            return int(row[employee_id_column]) == employee_id
        except ValueError:
            return False
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


#task 7

def sort_by_last_name():
    # column index func to find last names
    last_name_column = column_index("last_name")
    
    #call employees ["rows"] using sort method
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sorted_rows = sort_by_last_name()
print(employees)

#task 8

def employee_dict(row):
    return {
        field: row[index]
        for index, field in enumerate(employees["fields"])
        if field != "employee_id"
    }

#task 9

def all_employees_dict():
    #keys are employee id and values are from the dict
    result = {
        row[employee_id_column]: employee_dict(row)
        for row in employees["rows"]
    }
    return result

    #call def and print result
all_employees = all_employees_dict
print(all_employees)

#task 10
import os

def get_this_value():
    return os.getenv("THISVALUE")

value = get_this_value()
print(value)

#task 11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("swordfish")
print(custom_module.secret)

#task 12
#read csv and change rows to tuples
def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)

        rows = [tuple(row) for row in reader]
        return {"fields": fields, "rows": rows}

#main function read minutes
def read_minutes():
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    return minutes1, minutes2

#call def
minutes1, minutes2 = read_minutes()

print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

#task 13

def create_minutes_set():
    #change rows into sets
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    #combine into 1 set
    combine_set = set1.union(set2)

    return combine_set
minutes_set = create_minutes_set()

print("Minutes Set:", minutes_set)

#task 14

from datetime import datetime

def create_minutes_list():
    #create list from minutes set
    minutes_list = list(minutes_set)

    #use map to change each element
    #change each element into a tuple
    converted_list = list(
         map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )

    #return changes
    return converted_list
minutes_list = create_minutes_list()
print("Minutes List:", minutes_list)

#task 15

def write_sorted_list():

    #sort minutes list in acscending order of datetime
   
    sorted_list = sorted(minutes_list, key=lambda x:x[1])

    #call map to convert list to string for each tuple

    converted_list = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list)
    )

    #open minutes.csv to write data
    with open("./minutes.csv", mode="w") as file:
        writer = csv.writer(file)

    #write fields as first row from minutes1 dict
        writer.writerow(minutes1["fields"])

    #write next rows  
        writer.writerows(converted_list)
      
    #return converted list
    return converted_list






        

    














        

        
        
            
    

