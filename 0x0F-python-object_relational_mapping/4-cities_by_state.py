#!/usr/bin/python3
"""Script lists all cities in db hbtn_00_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM states JOIN cities ON cities.state_id = states.id \
                ORDER BY cities.id ASC;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
