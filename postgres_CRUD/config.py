from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/employee"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee_details'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    salary = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('email', name='uix_1'),)

# Create the table in the database
Base.metadata.create_all(engine)

def create_user(name, email,salary):
    existing_user = session.query(Employee).filter_by(email=email).first()
    if existing_user:
        print("User already exists!")
        return None
    
    new_user = Employee(name=name, email=email,salary=salary)
    session.add(new_user)
    try:
        session.commit()
        print("User created successfully!")
    except IntegrityError:
        session.rollback()
        print("User creation failed due to duplicate email!")
        return None
    return new_user

def get_user_by_email():
    users = session.query(Employee).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Salary: {user.salary}")

def update_user_email(user_id, new_email):
    user = session.query(Employee).get(user_id)
    if user:
        user.email = new_email
        try:
            session.commit()
            print("User updated successfully!")
        except IntegrityError:
            session.rollback()
            print("Update failed due to duplicate email!")
    else:
        print("User not found!")

def delete_user(user_id):
    user = session.query(Employee).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
    else:
        print("User not found!")

# create_user(name="Dhairya Bhagat", email="dhairya@example.com",salary="120000")
# get_user_by_email()
# update_user_email("1","dhruv@gmail.com")
# delete_user("2")