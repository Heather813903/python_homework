
import sqlite3

try:
    conn = sqlite3.connect("assignment7/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    print("Database connection established successfully.")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
);
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);    
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
);
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)

);
""")
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")


def connect_db():
    conn = sqlite3.connect("assignment7/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    return conn

def add_publisher(conn, name):
    try:
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}') already exists.")

def add_magazine(conn, name, publisher_name):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
    publisher = cursor.fetchone()
    if publisher :
        try:
            conn.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)" , (name, publisher[0]))
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
    else:
        print(f"Publisher '{publisher_name}' not found.")

def add_subscriber(conn, name, address):
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if cursor.fetchone():
        print("Subscriber '{name}' at '{address}' already exists.")
    else:
        conn.execute("INSERT INTO subscribers (name,address) Values (?, ?)" , (name,address))

def add_subscription(conn, subscriber_name, address, magazine_name, expiration_date):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, address))
    sub = cursor.fetchone()
    if not sub:
        print(f"Subscriber '{subscriber_name}' at '{address}' not found.")
        return
    subscriber_id = sub[0]

    cursor.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))
    mag = cursor.fetchone()
    if not mag:
        print(f"Magazine '{magazine_name}' not found.")
        return
    magazine_id = mag[0]

    cursor.execute("SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?" , (subscriber_id, magazine_id))
    if cursor.fetchone():
        print(f"Subscription already exists for '{subscriber_name}' to '{magazine_name}'.")
    else:
        conn.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)""", (subscriber_id, magazine_id, expiration_date))
        print(f"Added subscription: {subscriber_name} to {magazine_name} expires {expiration_date}")
        
conn = connect_db()

add_publisher(conn, "Sunny Days Publishing")
add_publisher(conn, "Curious Minds Press")
add_publisher(conn, "Everyday Life Media")
add_magazine(conn, "Happy Home","Sunny Days Publishing")
add_magazine(conn, "Kid Explorer","Curious Minds Press")   
add_magazine(conn, "The Daily Scoop","Everyday Life Media")
add_subscriber(conn, "Jenny Harper","22 Rosewood Lane")     
add_subscriber(conn, "Tommy Lewis","7 Bluebird Circle")  
add_subscriber(conn, "Nina Carter","15 Lakewood Drive")  
add_subscription(conn, "Jenny Harper","22 Rosewood Lane", "Happy Home", "2025-12-31")   
add_subscription(conn, "Tommy Lewis","7 Bluebird Circle", "The Daily Scoop", "2025-10-15")
add_subscription(conn, "Nina Carter","15 Lakewood Drive", "Kid Explorer","2025-09-03") 

conn.commit()
conn.close()
print("Data inserted successfully.")

# Task 4

def get_all_subscribers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers")
    rows = cursor.fetchall()
    print("All Subscribers:")
    for row in rows:
        print(row)
def get_all_magazines_sorted(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines ORDER by name")
    rows = cursor.fetchall()
    print("Magazines sorted by name:")
    for row in rows:
        print(row)
def get_magazines_by_publisher(conn, publisher_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT magazines.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.id
        WHERE publishers.name = ?
""", (publisher_name,))
    rows = cursor.fetchall()
    print(f"Magazines by '{publisher_name}':")
    for row in rows:
        print(row[0])


conn = connect_db()

get_all_subscribers(conn)
get_all_magazines_sorted(conn)
get_magazines_by_publisher(conn, "Sunny Days Publishing")

conn.close()


    
    






