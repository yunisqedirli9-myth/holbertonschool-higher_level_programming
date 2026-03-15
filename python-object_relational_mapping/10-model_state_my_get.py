#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Bağlantı mühərriki yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Sessiya yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Arqument olaraq göndərilən ştat adını (sys.argv[4]) axtarırıq
    # Bu format SQL Injection-dan tam qorunur
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Nəticəni yoxlayırıq
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
