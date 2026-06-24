import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/students.db")

avg_df = pd.read_sql_query("""
    SELECT name, ROUND(AVG(marks), 2) AS average
    FROM students
    GROUP BY name
    ORDER BY average DESC
""", conn)
conn.close()

# Bar chart of average marks
plt.figure(figsize=(8, 5))
plt.bar(avg_df["name"], avg_df["average"], color=["green", "red", "blue", "orange"])
plt.title("Average Marks Per Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.savefig("data/report.png")   # saves chart as image
plt.show()
print("Report saved to data/report.png")