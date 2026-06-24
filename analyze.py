import sqlite3
import pandas as pd

conn = sqlite3.connect("data/students.db")

# Average marks per student
avg_df = pd.read_sql_query("""
    SELECT name, ROUND(AVG(marks), 2) AS average
    FROM students
    GROUP BY name
    ORDER BY average DESC
""", conn)

# Topper per subject
topper_df = pd.read_sql_query("""
    SELECT subject, name, MAX(marks) AS top_marks
    FROM students
    GROUP BY subject
""", conn)

# Students who failed any subject (marks < 40)
fail_df = pd.read_sql_query("""
    SELECT name, subject, marks
    FROM students
    WHERE marks < 40
""", conn)

conn.close()

print("=== Average Marks ===")
print(avg_df)
print("\n=== Topper Per Subject ===")
print(topper_df)
print("\n=== Failed Students ===")
print(fail_df)