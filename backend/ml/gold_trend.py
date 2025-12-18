import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_price_range(days: int = 30):
    df = pd.read_csv("backend/ml/gold_prices.csv")

    # Sort by date
    df = df.sort_values("date").reset_index(drop=True)

    # Time index
    df["day_index"] = np.arange(len(df))

    X = df[["day_index"]]
    y = df["price"]

    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]

    # Volatility
    returns = df["price"].pct_change().dropna()
    volatility = returns.std()

    current_price = df["price"].iloc[-1]

    # Price range
    min_price = current_price * (1 - volatility * np.sqrt(days))
    max_price = current_price * (1 + volatility * np.sqrt(days))

    # Trend direction
    if slope > 0:
        trend = "bullish"
    elif slope < 0:
        trend = "bearish"
    else:
        trend = "sideways"

    # Trend strength (normalized slope)
    slope_strength = abs(slope) / current_price

    if slope_strength > 0.001:
        trend_strength = "strong"
    elif slope_strength > 0.0004:
        trend_strength = "moderate"
    else:
        trend_strength = "weak"

    # Confidence score (lower volatility = higher confidence)
    confidence = max(0, min(100, int((1 - volatility * 20) * 100)))

    # Signal
    if trend == "bullish" and trend_strength in ["strong", "moderate"]:
        signal = "buy_now_or_soon"
    elif trend == "bearish" and trend_strength == "strong":
        signal = "wait"
    else:
        signal = "neutral"

    return {
        "current_price": round(current_price, 2),
        "predicted_range": {
            "min": round(min_price, 2),
            "max": round(max_price, 2)
        },
        "trend": trend,
        "trend_strength": trend_strength,
        "volatility": round(volatility, 4),
        "confidence_score": confidence,
        "signal": signal,
        "days": days
    }
