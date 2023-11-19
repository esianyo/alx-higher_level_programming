#!/usr/bin/python3
"""checking for 'a'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./list_states_containing_a.py <mysql_username>\
              <mysql_password> <database_name>")
        exit(1)

    # Connect to the MySQL database
    engine = create_engine(f"mysql://{sys.argv[1]}:\
                           {sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for states containing the letter "a"
    states_containing_a = (
        session.query(State)
        .filter(State.name.contains("a")
                )
        .order_by(State.id)
    )

    # Print the results
    for state in states_containing_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
