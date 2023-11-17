#!/usr/bin/python3
"""class State"""

import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    select = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for s in select:
        print("{}: ({}) {}".format(s.State.name, s.City.id, s.state.name))
    session.commit()
