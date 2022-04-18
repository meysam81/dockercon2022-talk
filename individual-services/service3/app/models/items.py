import datetime

from app.database.orm import Base, BigInteger, Column, DateTime, Float, String


class Items(Base):
    __tablename__ = "items"

    # to avoid database-side computation, we generate the ID on the app-level
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False, default=0)
    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.datetime.utcnow().isoformat()
    )
    updated_at = Column(
        DateTime, nullable=False, default=lambda: datetime.datetime.utcnow().isoformat()
    )
