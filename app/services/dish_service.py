from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.models import Dish
from app.db.schemas import DishDto
import uuid
from datetime import datetime

def search_dish(db: Session, dish_name: str) -> tuple[DishDto, bool]:
    normalized = dish_name.replace("_", " ").lower()
    dish = (
        db.query(Dish)
        .filter(func.unaccent(func.lower(Dish.Name)).like(f"%{normalized}%"))
        .first()
    )

    if dish:
        return DishDto.model_validate(dish), True

    return DishDto(
        Id=uuid.uuid4(),
        Name=dish_name,
        Category="Unknown",
        Description="No description available.",
        Instructions="No instructions available.",
        CookingTime=0,
        Servings=0,
        ImageUrl="",
        Calories=0.0,
        Protein=0.0,
        Carbs=0.0,
        Fat=0.0,
        Fiber=0.0,
        Sugar=0.0,
        Ingredients="No ingredients listed.",
        CreatedAt=datetime.utcnow(),
        CreatedBy="predictor",
        ModifiedAt=datetime.utcnow(),
        ModifiedBy="predictor"
    ), False
