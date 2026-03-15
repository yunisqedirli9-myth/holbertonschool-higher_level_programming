#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (Safe from SQL injection).
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşuluruq
    # sys.argv[1]: username, sys.argv[2]: password, sys.argv[3]: db name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cursor = db.cursor()
    
    # SQL Injection-dan qorunmaq üçün %s yerləşdiricisindən istifadə edirik.
    # LIKE BINARY böyük/kiçik hərf həssaslığını (case-sensitive) təmin edir.
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    
    # Parametrləri tuple formatında (state_searched,) ötürürük
    cursor.execute(query, (sys.argv[4],))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
