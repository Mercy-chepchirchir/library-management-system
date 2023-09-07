# Importing Necessary Modules
import random
from faker import Faker
from  models import Session, Book, Journal, Student

def initialize_db():
    session = Session()
    
 #initializes an instance of the faker class which is sed to generate fake data
    fake = Faker()
    
  