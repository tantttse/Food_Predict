from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.model_loader import load_model
from app.services.predictor import predict_image
from app.services.dish_service import search_dish
from app.utils.response_builder import to_dish_response, wrap_dishes
from app.db.session import get_db
from app.core.redis_client import redis_client
import json, logging

router = APIRouter()
logger = logging.getLogger("predict")
model, idx_to_class = load_model()

@router.post("/predict")
async def predict(file: UploadFile = File(...), topk: int = 3, db: Session = Depends(get_db)):
    image_bytes = await file.read()
    results = predict_image(model, idx_to_class, image_bytes, topk)

    # cache key based on top dish
    top_dish = results[0]["dish"].lower()
    cache_key = f"prediction:wrapper:{top_dish}:top{topk}"

    cached = redis_client.get(cache_key)
    if cached:
        logger.info(f"Cache hit for key: {cache_key}")
        return JSONResponse(content=json.loads(cached))

    logger.info(f"Cache miss for key: {cache_key}. Querying repository.")
    
    # build fresh response
    dishes = []
    for result in results[:topk]:
        dto, matched = search_dish(db, result["dish"])
        dishes.append(to_dish_response(dto, result["confidence"], matched))

    wrapper = wrap_dishes(dishes)
    redis_client.set(cache_key, wrapper.model_dump_json(), ex=600)

    return wrapper
