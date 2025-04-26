#Task 5(6)

import sqlite3
import pandas as pd

with sqlite3.connect("./db/lesson.db") as conn:
    cursor = conn.cursor()
    sql_statement = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(sql_statement, conn)
print("First 5 rows of joined data:")
print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'

}).reset_index()

summary_df = summary_df.sort_values(by = 'product_name')
summary_df.to_csv("order_summary.csv", index = False)

print(summary_df.head())


