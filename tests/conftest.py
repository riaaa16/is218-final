'''
- Fixtures to run SQLAlchemy database tests on a local scale 
(using in-memory database)
- Fixture to run FastAPI tests.
'''
from unittest.mock import MagicMock
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from main import get_db, app

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
    # Creates a connection to database engine
    connection = engine.connect()
    # Creates a new transaction
    transaction = connection.begin()
    # Creates SQLAlchemy session bound to  connection
    session = sessionmaker(autocommit=False, autoflush=False,bind=connection)()

    yield session

    session.close()         # Closes session
    transaction.rollback()  # Rolls back transaction
    connection.close()      # Closes database connection

@pytest.fixture(scope="function")
def mock_get_db():
    '''
    Mock /score without the database functionality
    Database functionality tests can be seen in
    test_sqlalchemy.py
    '''
    # Create a mock session
    mock_session = MagicMock()

    # Mock methods on the session (like add, commit, and refresh)
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()
    mock_session.refresh = MagicMock()

    # Override the get_db dependency with our mock session
    app.dependency_overrides[get_db] = lambda: mock_session

    yield mock_session

    # Reset dependency overrides after the test
    app.dependency_overrides = {}
