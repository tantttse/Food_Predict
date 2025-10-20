from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from typing import List
 
class DishDto(BaseModel):
    Id: UUID
    Name: str
    Category: Optional[str]
    Description: Optional[str]
    Instructions: Optional[str]
    CookingTime: Optional[int]
    Servings: Optional[int]
    ImageUrl: Optional[str]
    Calories: float
    Protein: float
    Carbs: float
    Fat: float
    Fiber: float
    Sugar: float
    Ingredients: Optional[str]
    CreatedAt: Optional[datetime]
    CreatedBy: Optional[str]
    ModifiedAt: Optional[datetime]
    ModifiedBy: Optional[str]
    class Config:
        from_attributes = True
class NutritionInfo(BaseModel):
    calories: float
    protein: float
    carbs: float
    fat: float
    fiber: float
    sugar: float

class DishResponse(BaseModel):
    id: UUID
    name: str
    category: Optional[str]
    description: Optional[str]
    instructions: Optional[str]
    cookingTime: Optional[int]
    servings: Optional[int]
    imageUrl: Optional[str]
    ingredients: Optional[str]
    nutritionInfo: NutritionInfo
    confidence: Optional[float] = None   
    matched: Optional[bool] = None
class DishesWrapper(BaseModel):
    dishes: List[DishResponse]
