import sqlite3

# Connect to database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sales_data = [
    ("Laptop", 5, 50000),
    ("Mobile", 10, 20000),
    ("Tablet", 3, 15000)
]

cursor.executemany(
    "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
    sales_data
)

conn.commit()

# Query data
cursor.execute("""
SELECT product,
       quantity,
       price,
       quantity * price AS total_sales
FROM sales
""")

results = cursor.fetchall()

print("Sales Report")
print("-" * 40)

for row in results:
    print(
        f"Product: {row[0]}, Qty: {row[1]}, Price: {row[2]}, Total: {row[3]}"
    )

conn.close()
