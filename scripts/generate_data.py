import pandas as pd
import numpy as np

np.random.seed(42)

GST = 0.03

records = []

for _ in range(5000):
    gold_rate = np.random.uniform(5500, 7500)
    weight = np.random.uniform(2, 60)
    making_pct = np.random.uniform(10, 30)
    wastage_pct = np.random.uniform(5, 15)

    effective_weight = weight * (1 + wastage_pct / 100)
    base_price = effective_weight * gold_rate

    making_charge = base_price * (making_pct / 100)
    gst = (base_price + making_charge) * GST

    final_price = base_price + making_charge + gst

    records.append([
        gold_rate, weight, making_pct, wastage_pct, final_price
    ])

df = pd.DataFrame(records, columns=[
    "gold_rate", "weight", "making_pct", "wastage_pct", "price"
])

df.to_csv("data/jewellery_price_india.csv", index=False)
print("Dataset generated:", df.shape)

