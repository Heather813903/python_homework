import sqlite3
with sqlite3.connect("assignment7/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    print("Database created and connected successfully.")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER,
        major TEXT
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
        instructor_name TEXT
)
""")
    
    cursor.execute("DROP TABLE IF EXISTS Enrollments")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL, 
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Students(id),
        FOREIGN KEY (course_id) REFERENCES Courses(id)
)
""")
    
    print("Tables created successfully.")
