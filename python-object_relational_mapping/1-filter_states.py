#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cursor = db.cursor()
    
    # 'N' (böyük hərf) ilə başlayanları tapmaq üçün BINARY istifadə edirik
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
