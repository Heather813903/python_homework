

# Connect to the database
import sqlite3
with sqlite3.connect("assignment7/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()

    
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Bob', 22, 'History')")
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')")

    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')")
    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')")

    
    conn.commit()

    print("Sample data inserted successfully.")

import sqlite3

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

with sqlite3.connect("assignment7/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")



cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
result = cursor.fetchall()
for row in result:
        print(row)

def enroll_students(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,))
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course names{course}.")
        return
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?,?)", (student_id, course_id))

    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
      print(f"Student {student} is already enrolled in course {course}.")
      
   
with sqlite3.connect("assignment7/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")   
    cursor = conn.cursor()

    enroll_students(cursor, "Alice", "Math 101")
    enroll_students(cursor, "Alice", "Chemistry 101")
    enroll_students(cursor, "Bob", "Math 101")
    enroll_students(cursor, "Bob", "English 101")
    enroll_students(cursor, "Charlie", "English 101")

    conn.commit()  
    cursor.execute("PRAGMA table_info(Students);")
    print("Students table schema:")
    for row in cursor.fetchall():
        print(row)
        cursor.execute("PRAGMA table_info(Enrollments);")
    print("Enrollments table schema:")
    for row in cursor.fetchall():
        print(row)
    
    # Check foreign keys in Enrollments
    cursor.execute("PRAGMA foreign_key_list(Enrollments);")
    print("Foreign key constraints in Enrollments:")
    for row in cursor.fetchall():
        print(row)


    
  #  enroll_students(cursor, "Alice", "Math 101")
  #  enroll_students(cursor, "Alice", "Chemistry 101")
  #  enroll_students(cursor, "Bob", "Math 101")
  #  enroll_students(cursor, "Bob", "English 101")
  #  enroll_students(cursor, "Charlie", "English 101")
  #  conn.commit() 

  


    
    


