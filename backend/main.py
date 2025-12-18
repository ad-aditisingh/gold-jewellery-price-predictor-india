from fastapi import FastAPI
from pydantic import BaseModel

from backend.pricing.deterministic import calculate_today_price
from backend.ml.gold_trend import predict_price_range

app = FastAPI(title="Gold Jewellery Intelligence API")

class TodayPriceRequest(BaseModel):
    rate: float
    rate_unit: str
    purity: str
    weight: float
    making_type: str
    making_value: float

@app.post("/price/today")
def today_price(data: TodayPriceRequest):
    return calculate_today_price(
        data.rate,
        data.rate_unit,
        data.purity,
        data.weight,
        data.making_type,
        data.making_value
    )

@app.get("/price/outlook")
def price_outlook(days: int = 30):
    return predict_price_range(days)
