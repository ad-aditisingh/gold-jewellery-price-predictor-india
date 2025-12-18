import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_price_range(days: int = 30):
    df = pd.read_csv("backend/ml/gold_prices.csv")

    # Ensure correct order
    df = df.sort_values("date").reset_index(drop=True)

    df["day_index"] = np.arange(len(df))

    X = df[["day_index"]]
    y = df["price"]

    model = LinearRegression()
    model.fit(X, y)

    last_day = df["day_index"].iloc[-1]

    future_days = np.arange(
        last_day + 1,
        last_day + days + 1
    ).reshape(-1, 1)

    # Regression forecast (used only for trend)
    _ = model.predict(future_days)

    # Volatility-based range
    returns = df["price"].pct_change().dropna()
    volatility = returns.std()

    current_price = df["price"].iloc[-1]

    min_price = current_price * (1 - volatility * np.sqrt(days))
    max_price = current_price * (1 + volatility * np.sqrt(days))

    slope = model.coef_[0]
    if slope > 0:
        trend = "bullish"
    elif slope < 0:
        trend = "bearish"
    else:
        trend = "sideways"

    return {
        "current_price": round(current_price, 2),
        "predicted_range": {
            "min": round(min_price, 2),
            "max": round(max_price, 2)
        },
        "trend": trend,
        "volatility": round(volatility, 4),
        "days": days
    }
