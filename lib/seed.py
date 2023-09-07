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
        
        # Create a Book object with the generated data.
        book = Book(
            book_id=book_id_value,
            title=fake.catch_phrase(),
            author=fake.name(),
            total_copies=total_copies_number,
            #rendint returns a random integer value between the two lower and higher limits
            available_copies=random.randint(1, total_copies_number),
            fee_per_day=10
        )
        
        session.add(book) #Add the book object to the database session
        