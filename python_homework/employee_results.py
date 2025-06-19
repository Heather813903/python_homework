#Task 1

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

import os
print("Looking for DB at:", os.path.abspath("../db/lesson.db"))
print("Exists:", os.path.exists("../db/lesson.db"))

#Connect to db
conn = sqlite3.connect("../db/lesson.db")


#SQL query
df = pd.read_sql_query("""
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
""", conn)


#Close db
conn.close()

#Plot
plt.figure(figsize=(10, 6))
df.plot(kind='bar', x='last_name', y='revenue', color='skyblue', legend=False)
plt.title("Employee Revenue from Sales")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

