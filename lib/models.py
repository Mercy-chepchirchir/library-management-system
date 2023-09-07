# Import necessary SQLAlchemy modules
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///library.db')

# Create a base class for declarative models
Base = declarative_base()


# used to interact with the database
Session = sessionmaker(bind=engine)

# Define the Book class with attributes and relationships
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    total_copies = Column(Integer, nullable=False, default=1)
    available_copies = Column(Integer, nullable=False, default=1)
    fee_per_day = Column(Float, default=0.00)  # Adjust fee as needed

    book_transactions = relationship('BookTransaction', back_populates='book')
    