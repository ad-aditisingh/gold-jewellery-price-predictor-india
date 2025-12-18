GST = 0.03

PURITY_MAP = {
    "22K": 0.916,
    "18K": 0.750,
    "9K": 0.375
}

def calculate_today_price(
    rate: float,
    rate_unit: str,
    purity: str,
    weight: float,
    making_type: str,
    making_value: float
):
    # Normalize rate to per gram
    if rate_unit == "10g":
        rate_per_gram = rate / 10
    elif rate_unit == "100g":
        rate_per_gram = rate / 100
    else:
        rate_per_gram = rate

    # Adjust purity (assume input rate is 22K)
    effective_rate = rate_per_gram * (
        PURITY_MAP[purity] / PURITY_MAP["22K"]
    )

    gold_value = effective_rate * weight

    if making_type == "percentage":
        making_charge = gold_value * (making_value / 100)
    else:
        making_charge = making_value * weight

    subtotal = gold_value + making_charge
    gst = subtotal * GST

    return {
        "gold_value": round(gold_value, 2),
        "making_charge": round(making_charge, 2),
        "gst": round(gst, 2),
        "final_price": round(subtotal + gst, 2)
    }
