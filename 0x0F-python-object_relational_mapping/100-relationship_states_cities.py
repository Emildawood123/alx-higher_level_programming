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
    state1 = State(name="California")
    city1 = City(name="San Francisco", state=state1)
    state1.cities.append(city1)
    session.add(state1)
    session.commit()
