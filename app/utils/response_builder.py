from app.db.schemas import DishDto, DishResponse, NutritionInfo, DishesWrapper

def to_dish_response(dish: DishDto, confidence: float, matched: bool) -> DishResponse:
    return DishResponse(
        id=dish.Id,
        name=dish.Name,
        category=dish.Category,
        description=dish.Description,
        instructions=dish.Instructions,
        cookingTime=dish.CookingTime,
        servings=dish.Servings,
        imageUrl=dish.ImageUrl,
        ingredients=dish.Ingredients,
        nutritionInfo=NutritionInfo(
            calories=dish.Calories,
            protein=dish.Protein,
            carbs=dish.Carbs,
            fat=dish.Fat,
            fiber=dish.Fiber,
            sugar=dish.Sugar
        ),
        confidence=round(confidence, 4),
        matched=matched
    )

def wrap_dishes(dishes: list[DishResponse]) -> DishesWrapper:
    return DishesWrapper(dishes=dishes)
