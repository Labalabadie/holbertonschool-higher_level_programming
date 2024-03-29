#!/usr/bin/python3
"""List every state.name with a letter 'a'
to the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states_list = session.query(State).filter(State.name.like('%a%')).all()
    if states_list:
        for state in states_list:
            print("{}: {}".format(state.id, state.name))
    session.close()
