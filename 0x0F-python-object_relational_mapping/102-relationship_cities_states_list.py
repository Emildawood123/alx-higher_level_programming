#!/usr/bin/python3
"""import some libraries"""

import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    selectState = session.query(City, State).filter(
        State.cities).order_by(City.id).all()
    for s in selectState:
        print("{}: {} -> {}".format(s.City.id, s.City.name, s.State.name))
