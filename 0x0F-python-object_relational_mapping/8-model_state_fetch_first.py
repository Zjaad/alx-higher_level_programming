#!/usr/bin/python3
"""Display the 1st State obj from the DB."""
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
    fS = sn.query(State).order_by(State.id).first()
    if fS:
        print("{}: {}".format(fS.id, fS.name))
    else:
        print("Nothing")
    sn.close()