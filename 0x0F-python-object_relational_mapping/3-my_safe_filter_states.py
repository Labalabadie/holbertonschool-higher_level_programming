#!/usr/bin/python3
"""Script lists all states in db hbtn_00_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name=%(arg_state)s\
            ORDER BY states.id ASC", {'arg_state': argv[4]})
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
