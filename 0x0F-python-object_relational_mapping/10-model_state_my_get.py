#!/usr/bin/python3
"""Display State obj with the nname passed as an arg"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    SN = sessionmaker(bind=engine)
    sn = SN()
    qs = sn.query(State).filter(State.name == sys.argv[4]).first()
    if qs:
        print(qs.id)
    else:
        print("Not found")
    sn.close()
