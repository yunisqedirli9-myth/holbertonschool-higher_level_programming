#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Arqumentlərdən istifadə edərək bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # Ştat adına görə şəhərləri tapmaq üçün JOIN sorğusu
    query = "SELECT cities.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s " \
            "ORDER BY cities.id ASC"
    
    cursor.execute(query, (sys.argv[4],))
    
    # Bütün nəticələri alırıq
    rows = cursor.fetchall()
    
    # Şəhər adlarını vergüllə ayıraraq çap edirik
    print(", ".join(row[0] for row in rows))
    
    cursor.close()
    db.close()
