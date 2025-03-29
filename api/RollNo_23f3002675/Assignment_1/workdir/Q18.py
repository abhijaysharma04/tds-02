import sqlite3
import os

# Full absolute path to your DB
db_path = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\ticket-sales.db"

if not os.path.exists(db_path):
    print(f"❌ File not found: {db_path}")
    exit()

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Case-insensitive match for 'gold'
    query = """
    SELECT SUM(units * price)
    FROM tickets
    WHERE LOWER(type) = 'gold';
    """

    cursor.execute(query)
    result = cursor.fetchone()[0]

    if result:
        print(f"✅ Total sales for Gold tickets: {result:.2f}")
    else:
        print("⚠️ No Gold ticket sales found.")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if conn:
        conn.close()
