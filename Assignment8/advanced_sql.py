import sqlite3

try:
    def setup_database(cursor):
    # Create Tables
        cursor.execute("""  
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        order_date TEXT NOT NULL,
        customer_id INTEGER, 
        employee_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )""")          

        cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )""")

        cursor.execute("""
    CREATE TABLE IF NOT EXISTS line_items (
        line_item_id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )""")

        cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    )""")
    
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )""")

    # Insert Sample Data if not already present

        cursor.execute("SELECT COUNT(*) FROM customers")
        if      cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO customers (customer_id, customer_name) VALUES (?, ?)", [
            (1, 'Alice'),
            (2, 'Bob'),
            (3, 'Charlie'),
            (4, 'Perez and Sons')
        ])

        cursor.execute("SELECT COUNT(*) FROM employees")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO employees (employee_id, first_name, last_name) VALUES (?, ?, ?)", [
            (1, 'John', 'Smith'),
            (2, 'Miranda', 'Harris'), 
            (3, 'Laura', 'Jones')
        ])

        cursor.execute("SELECT COUNT(*) FROM orders")
        if cursor.fetchone()[0] == 0:   
            cursor.executemany("INSERT INTO orders (order_id, order_date, customer_id, employee_id) VALUES (?, ?, ?, ?)", [
            (1, '2023-01-01', 1, 1),
            (2, '2023-01-02', 1, 1),
            (3, '2023-01-03', 2, 1),
            (4, '2023-01-04', 2, 1),
            (5, '2023-01-05', 3, 1),
            (6, '2023-01-06', 3, 1),
            (7, '2023-01-07', 3, 2),
            (8, '2023-01-08', 4, 2),
            (9, '2023-01-09', 4, 2),
            (10, '2023-01-10', 2, 3)
        ])

        cursor.execute("SELECT COUNT(*) FROM products")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)", [
            (1, 'Product A', 10.00),
            (2, 'Product B', 20.00),
            (3, 'Product C', 30.00),
            (4, 'Product D', 40.00),
            (5, 'Product E',  5.00),
            (6, 'Product F',  8.00)
        ])       

        cursor.execute("SELECT COUNT(*) FROM line_items")
        if cursor.fetchone()[0] == 0:
         cursor.executemany("INSERT INTO line_items (line_item_id, order_id, product_id, quantity) VALUES (?, ?, ?, ?)", [
            (1, 1, 1, 2), 
            (2, 1, 2, 1),
            (3, 2, 2, 3),
            (4, 3, 3, 1),
            (5, 4, 1, 1),
            (6, 5, 4, 2),
            (7, 6, 2, 2),
            (8, 7, 1, 1),
            (9, 8, 3, 1),
            (10, 9, 5, 3),
            (11, 10, 6, 4)
        ])

 
    def employees_with_more_than_5_orders(cursor):
        stmt="""SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) as count
          FROM employees e 
          JOIN orders o ON e.employee_id = e.employee_id
          GROUP BY e.employee_id
          HAVING COUNT(order_id) > 5;"""
        
 
        cursor.execute(stmt)
        results = cursor.fetchall()

        print("\nTask 4: Employees With More Than 5 Orders")
        print("Employee ID | First Name | Last Name | Order Count")
        print("----------------------------------------------------")
        for row in results:
            print(row)
            

    conn = sqlite3.connect("company.db") 
    conn.execute("PRAGMA foreign_keys = 1") # Replace with your actual DB
    cursor = conn.cursor()
    setup_database(cursor)
    
    
    conn.commit()

    employees_with_more_than_5_orders(cursor)

    conn.close()

except sqlite3.OperationalError as e:
    print("SQLite OperationalError:", e)
    print("Hint: Check your table and column names for typos or mismatches.")

except sqlite3.Error as e:
    print("Database error occurred:", e)

except Exception as e:
    print("Unexpected error:", e)

    


#cursor.execute("PRAGMA table_info(orders)")
#print("Orders Table Schema:")
#for column in cursor.fetchall():
#    print(column)

#cursor.execute("PRAGMA table_info(employees)")
#print("\nEmployees Table Schema:")
#for column in cursor.fetchall():
#    print(column)