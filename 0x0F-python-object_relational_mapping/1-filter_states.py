#!/usr/bin/python3
"""Script lists all states in db hbtn_00_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE states.name REGEXP '^[N].*$' \
                ORDER BY states.id ASC;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
