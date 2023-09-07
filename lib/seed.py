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
        session.commit() #persists data in the database
        
        #Add the generated book_id to the 'books' list.
        books.append(book_id_value)
        
        #Increase the book_id number for the next iteration.
        book_id_number = book_id_number + 1
        
    journals = [] #initialize an empty list journal where the generated journal id will be stored
    journal_id_number = 1

    for item in range(100):
        journal_id_value = f"J0{journal_id_number}"
        #generate a random integer between 1 and 100, representing the total number of copies of this journal.
        total_copies_number = random.randint(1, 100)
        
        journal = Journal(
            journal_id=journal_id_value,
            title=fake.catch_phrase(),
            editor=fake.name(),
            total_copies=total_copies_number,
            available_copies=random.randint(1, total_copies_number),
            fee_per_day=10
        )
        session.add(journal)#Add the journal object to the database session
        session.commit()#persists data in the database
        