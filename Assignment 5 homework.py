import pandas as pd
data = [{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000}, \
{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003}, \
{'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500}, \
{'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}]
sales = pd.DataFrame(data)
print(sales)

sales_pivot1 = pd.pivot_table(sales,index=['Product', 'Region'],values=['Revenue'],aggfunc='sum',fill_value=0)
print(sales_pivot1)

sales_pivot2 = pd.pivot_table(sales,index='Product',values='Revenue', columns='Region',aggfunc='sum',fill_value=0)
print(sales_pivot2)

sales_pivot3 = pd.pivot_table(sales,index='Product',values='Revenue',columns=['Region','Employee'], aggfunc='sum',fill_value=0)
print(sales_pivot3)

sales_pivot2['Total'] = sales_pivot2['East'] + sales_pivot2['West']
print(sales_pivot2)
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Percentage'] = [0.12, 0.09, 0.1]
per_employee_sales['Commission'] = per_employee_sales['Revenue'] * per_employee_sales['Commission Percentage']
print(per_employee_sales)

per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A','A','B']

def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)
    
per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)
print(per_employee_sales)

import pandas as pd


data = {'Name': ['Alice', 'Bob', 'None', 'David'],
        'Age' : [24, 27, 22, None],
        'Score' : [85, None, 88, 76]
}
df = pd.DataFrame(data)

df_missing = df[df.isnull().any(axis=1)]
print(df_missing)  

df_dropped = df.dropna()
print(df_dropped)

df_filled = df.fillna({'Age': 0, 'Score' : df['Score'].mean()})
print(df_filled)

import pandas as pd
data = {'Name': ['Alice','Bob','Charlie'],
        'Age' : ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']
        }
df = pd.DataFrame(data)

df['Age'] = df["Age"].astype(int)

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)
print(df)

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location' : ['LA', 'LA', 'NY'],
        'JoinDate' : ['2023-01-15', '2022-12-20', '2023-03-01']
        }
df = pd.DataFrame(data)
df['Location'] = df['Location'].map({'LA' : 'Los Angeles', 'NY':'New York'})
print(df)

import pandas as pd
data = {'Name': ['Tom','Dick','Harry','Mary'], 'Phone':[3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
            if len(out_string) == 10:
                return out_string
            return None
    df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
    print(df)

    import pandas as pd
data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
print(df)

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age' : [20, 22, 43]
        }

df =pd.DataFrame(data)
df['Age'] = df['Age'] +1
print(df)

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]
    }
df = pd.DataFrame(data)
df['Grade'] = pd.cut(df['Grade'], 3, labels = ["bad", "okay", "great"])
print(df)

import pandas as pd

# Sample DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df = pd.DataFrame(data)

# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print(df_cleaned_by_name)


import pandas as pd

data = {'Name': ['Alice', None, 'Charlie', 'David'],
        'Age': [24, None, 22, 35],
        'Salary': [50000, 60000, None, None]
}
df = pd.DataFrame(data)
print(df)
