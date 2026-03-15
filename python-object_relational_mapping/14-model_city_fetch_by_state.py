#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Verilənlər bazasına qoşuluruq
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # State və City cədvəllərini birləşdirib (JOIN), City ID-sinə görə sıralayırıq
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    
    # Nəticələri "State Name: (City ID) City Name" formatında çap edirik
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        
    session.close()
