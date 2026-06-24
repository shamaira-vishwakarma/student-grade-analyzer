import sqlite3

conn = sqlite3.connect("data/students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        name TEXT,
        subject TEXT,
        marks INTEGER
    )
""")

# Sample data
students = [
    (1, "Shamaira", "Maths", 88),
    (1, "Shamaira", "Physics", 74),
    (1, "Shamaira", "Python", 95),
    (2, "Rahul", "Maths", 45),
    (2, "Rahul", "Physics", 38),
    (2, "Rahul", "Python", 60),
    (3, "Priya", "Maths", 92),
    (3, "Priya", "Physics", 88),
    (3, "Priya", "Python", 97),
    (4, "Arjun", "Maths", 55),
    (4, "Arjun", "Physics", 62),
    (4, "Arjun", "Python", 49),
]

# Insert data
cursor.executemany(
    "INSERT INTO students (student_id, name, subject, marks) VALUES (?, ?, ?, ?)",
    students
)

conn.commit()
conn.close()

print("Database created and populated!")