import math
#The work here is verified and developed by Zioles(Dhrruv)

def trig_ratios(angle_deg):
    angle_rad = math.radians(angle_deg)
    return {
        "Sine": math.sin(angle_rad),
        "Cosine": math.cos(angle_rad),
        "Tangent": math.tan(angle_rad)
        if angle_deg % 180 != 90 else "Undefined"
    }


print("--- Class 10 Math: Trigonometry Tool ---")
angle = float(input("Enter angle in degrees:"))
results = trig_ratios(angle)

for ratio, value in results.items():
    if isinstance(value, float):
        print(f"{ratio}: {value:.4f}")
    else:
        print(f"{ratio}: {value}")
