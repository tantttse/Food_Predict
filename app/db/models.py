from sqlalchemy import Column, String, Integer, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class Dish(Base):
    __tablename__ = "Dishes"  # Case-sensitive match

    Id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name = Column(String, nullable=False)
    Category = Column(String)
    Description = Column(String)
    Instructions = Column(Text)
    CookingTime = Column(Integer)
    Servings = Column(Integer)
    ImageUrl = Column(String)

    Calories = Column(Float)
    Protein = Column(Float)
    Carbs = Column(Float)
    Fat = Column(Float)
    Fiber = Column(Float)
    Sugar = Column(Float)

    Ingredients = Column(Text)
    CreatedAt = Column(DateTime(timezone=True))
    CreatedBy = Column(Text)
    ModifiedAt = Column(DateTime(timezone=True))
    ModifiedBy = Column(Text)
