from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine('mysql://username:password@localhost:3306/database_name')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()

# Declare a Base class using the declarative_base function
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Print the SQL CREATE statements
print(Base.metadata.create_all(engine))
