import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/jewellery_price_india.csv")

X = df[["gold_rate", "weight", "making_pct", "wastage_pct"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "linear_regression_jewellery_model.pkl")
print("Model trained and saved")
