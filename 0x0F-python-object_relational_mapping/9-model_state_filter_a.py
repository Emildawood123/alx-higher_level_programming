#!/usr/bin/python3
"""class State"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    sid = State.id
    sna = State.name
    result = session.query(State).order_by(sid).filter(sna.like("%a%")).all()

    for state in result:
        print(f"{state.id}: {state.name}")
