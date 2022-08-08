#!/usr/bin/python3
"""prints all City objects
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    cities_list = session.query(City, State)\
                            .filter(City.state_id == State.id)\
                            .order_by(City.id)\
                            .all()
    for state, city in cities_list:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
    session.close()
