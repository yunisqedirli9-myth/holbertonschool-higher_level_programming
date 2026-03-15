#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # SQL Injection-dan qorunmaq üçün %s istifadə edirik
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))
    
    # Şəhər adlarını bir sətirdə vergüllə ayıraraq çap edirik
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    
    cursor.close()
    db.close()
