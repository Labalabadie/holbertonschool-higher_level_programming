#!/usr/bin/python3
"""Script lists all states in db hbtn_00_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name=%(arg_state)s\
            ORDER BY states.id ASC", {'arg_state': argv[4]})
    states = cur.fetchall()
    for i in range(len(states)):
        print(str(states[i][0]), end="")
        if i != (len(states) - 1):
            print(", ", end="")
        else:
            print()
        cur.close()
    db.close()
