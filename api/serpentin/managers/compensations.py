from serpentin.models.compensations import Compensation

def get_compensations():
    return Compensation.objects()

def apply_compensation_to_deals(sales, compensation, deals):
    if compensation.type == "Simple":
        return apply_simple_compensation(sales, deals)
    elif compensation.type == "Complex":
        return apply_complex_compensation(sales, deals)

def apply_simple_compensation(sales, deals):
    total = sum([d.amount for d in deals if d.closed])
    coefficient = 0.2 if len(deals) > 4 else 0.1
    return max(coefficient * total, 500)

def apply_complex_compensation(sales, deals):
    compensation_steps = [
        { "lower": 0,   "upper": 0.5,          "coefficient": 0    },
        { "lower": 0.5, "upper": 1,            "coefficient": 0.08 },
        { "lower": 1,   "upper": 1.5,          "coefficient": 0.12 },
        { "lower": 1.5, "upper": float('inf'), "coefficient": 0.16 }
    ]
    target = sales.target
    total = sum([d.amount for d in deals if d.closed])
    compensation = sum([s["coefficient"] * max(0, min(total, target * s["upper"]) - target * s["lower"]) for s in compensation_steps])
    if len(deals) > 7:
        compensation += 500
    return compensation
