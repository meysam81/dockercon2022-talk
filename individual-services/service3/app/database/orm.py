from sqlalchemy import BigInteger, Column, DateTime, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connection(conn_string: str):
    """
    conn_string = "sqlite:///./sql_app.db"
    conn_string = "postgresql://user:password@postgresserver/db"
    """
    kwargs = {}
    if conn_string.startswith("sqlite"):
        kwargs.update(connect_args={"check_same_thread": False})
    engine = create_engine(conn_string, **kwargs)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()


Base = declarative_base()


__all__ = [
    "BigInteger",
    "String",
    "Float",
    "DateTime",
    "Column",
]
