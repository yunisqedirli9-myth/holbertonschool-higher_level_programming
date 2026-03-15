#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument.
This script is safe from MySQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # SQL injection-dan qorunmaq üçün parametrli sorğu:
    # SQL mühərriki %s yerinə gələn datanı birbaşa string kimi təmizləyir.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()
