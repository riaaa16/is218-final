'''
- Fixtures to run SQLAlchemy database tests on a local scale 
(using in-memory database)
- Fixture to run FastAPI tests.
'''
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.models import Base
from main import app

@pytest.fixture(scope="session")
def client():
    '''
    Fixture creating a TestClient for FastAPI
    Scope is per pytest
    '''
    with TestClient(app) as client:
        yield client # Let test functions use TestClient instance

@pytest.fixture(scope="session")
def engine():
    """
    Fixture creating a SQLAlchemy engine connected to an in-memory test database.
    Scope is per pytest
    """
    # Use an in-memory SQLite database for tests
    # Once test session is done, database is discarded
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="session", autouse=True)
def tables(engine):
    """
    Fixture to create database tables.
    Scope is per pytest"""
    Base.metadata.create_all(engine)    # Attack table is created
    yield
    Base.metadata.drop_all(engine)      # Attack table is removed

@pytest.fixture(scope="function")
def db_session(engine):
    """
    Fixture to create a SQLAlchemy session for tests.
    Scope is per function in pytest"""
    connection = engine.connect()               # Creates a connection to database engine
    transaction = connection.begin()            # Creates a new transaction
    session = sessionmaker(bind=connection)()   # Creates SQLAlchemy session bound to  connection

    yield session

    session.close()         # Closes session
    transaction.rollback()  # Rolls back transaction
    connection.close()      # Closes database connection
