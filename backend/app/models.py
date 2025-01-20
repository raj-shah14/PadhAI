from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection settings
DATABASE_URL = "postgresql://rajshah:padhaikarlo@localhost/padhai"

# Create a new base class for SQLAlchemy models
Base = declarative_base()

# Create an engine that stores data in the PostgreSQL database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal will be used to create session instances to interact with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)