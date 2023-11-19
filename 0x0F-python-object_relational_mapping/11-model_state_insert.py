#!/usr/bin/python3
"""insert to state table"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    eng = create_engine(connection.format(user_name, password, db_name),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    state_to_add = State(name="Louisiana")
    session.add(state_to_add)
    session.commit()
    obj = session.query(State).filter_by(name="Louisiana").first()
    print(obj.id)
