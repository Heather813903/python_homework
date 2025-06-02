# Task 2

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connect to db
conn = sqlite3.connect("./db/lesson.db")

#SQL query to get total price
df = pd.read_sql_query("""
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
""", conn)

# Close db
conn.close

# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

#Plot
plt.figure(figsize=(10, 6))
df.plot(x='order_id', y='cumulative', kind='line', color='green', legend=False)
plt.title("Cumulative Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(True)
plt.show()




