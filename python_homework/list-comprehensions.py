#Task 3

import pandas as pd

csv_path = "./csv/employees.csv"
df = pd.read_csv(csv_path)

print(df.head())

# create a list of the employee names, first_name + space + last_name.
full_names = [row['first_name'] + " " + row['last_name'] for _, row in df.iterrows()]
print("All Employees Names:")
print(full_names)



#create another list from the previous list of names. This list should include only those names that contain the letter "e". Print this list.
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nEmployee Names Containing 'e':")
print(names_with_e)