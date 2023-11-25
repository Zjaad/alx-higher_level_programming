#!/usr/bin/python3
"""Display all states that contain the letter 'a'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    SN = sessionmaker(bind=engine)
    sn = SN()
    AinS = sn.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for s in AinS:
        print("{}: {}".format(s.id, s.name))
    sn.close()
