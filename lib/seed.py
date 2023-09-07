# Importing Necessary Modules
import random
from faker import Faker
from  models import Session, Book, Journal, Student

def initialize_db():
    session = Session()
    
 # Generating Fake Data for Books:
    fake = Faker()
    
    books = []
    book_id_number = 1 #initialize the book id number to start at 1
    for item in range(100):
        book_id_value = f"B0{book_id_number}"
        total_copies_number = random.randint(1, 100)
        
  