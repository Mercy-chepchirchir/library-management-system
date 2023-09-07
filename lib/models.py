# Import necessary SQLAlchemy modules
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///library.db')
